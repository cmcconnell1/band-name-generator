"""Command-line interface for band name generator.

This module provides the CLI for generating band names with various patterns.
Users can generate random names, specify patterns, and control the number of
names generated.

Usage:
    python -m band_name_generator                    # Generate 1 random name
    python -m band_name_generator -n 10              # Generate 10 names
    python -m band_name_generator -p metal_noun      # Use specific pattern
    python -m band_name_generator -l                 # List available patterns
    python -m band_name_generator --random           # Continuous random mode
"""

import argparse
import signal
import sys
import time

from .generator import BandNameGenerator
from .patterns import BandNamePattern


def main() -> int:
    """Main CLI entry point for the band name generator.

    Parses command-line arguments and generates band names based on user input.
    Supports three main modes:
    1. List patterns mode (-l/--list-patterns): Display all available patterns
    2. Pattern mode (-p/--pattern): Generate names using a specific pattern
    3. Random mode (default): Generate names using random patterns

    Command-line Arguments:
        -n, --count (int): Number of band names to generate (default: 1)
        -p, --pattern (str): Specific pattern to use (optional)
        -l, --list-patterns: List all available patterns and exit

    Returns:
        Exit code (0 for success, non-zero for errors)

    Examples:
        >>> # Generate 1 random band name
        >>> main()  # Called with no arguments
        Generated band name:
          Iron Maiden

        >>> # Generate 5 metal-themed names
        >>> main()  # Called with ['-p', 'metal_noun', '-n', '5']
        Generated 5 band names:
          1. Iron Maiden
          2. Steel Dragon
          ...
    """
    # Set up argument parser with help text and examples
    parser = argparse.ArgumentParser(
        description="Generate random band names like Depeche Mode, Iron Maiden, Limp Bizkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Generate 1 random band name
  %(prog)s -n 10              # Generate 10 random band names
  %(prog)s -p adjective_noun  # Use specific pattern
  %(prog)s -l                 # List all available patterns
        """,
    )

    # Add argument for number of names to generate
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=None,
        help="Number of band names to generate (default: 1 for normal mode, infinite for --random mode)",
    )

    # Add argument for specifying a pattern
    parser.add_argument(
        "-p",
        "--pattern",
        type=str,
        choices=[p.value for p in BandNamePattern],
        help="Specific pattern to use (random if not specified)",
    )

    # Add argument for listing available patterns
    parser.add_argument(
        "-l",
        "--list-patterns",
        action="store_true",
        help="List all available patterns and exit",
    )

    # Add argument for random continuous mode
    parser.add_argument(
        "-r",
        "--random",
        action="store_true",
        help="Continuous random mode - generate names indefinitely (Ctrl+C to stop)",
    )

    # Add argument for interval between names in random mode
    parser.add_argument(
        "-i",
        "--interval",
        type=float,
        default=5.0,
        help="Seconds between names in random mode (default: 5.0)",
    )

    # Parse command-line arguments
    args = parser.parse_args()

    # Handle list patterns mode - display all patterns and exit
    if args.list_patterns:
        print("Available patterns:")
        print("\nTwo-word patterns:")
        # Display two-word patterns (e.g., adjective_noun, metal_noun)
        for pattern in BandNamePattern.two_word_patterns():
            print(f"  - {pattern.value}")
        print("\nMulti-word patterns:")
        # Display multi-word patterns not already shown in two-word section
        for pattern in BandNamePattern.multi_word_patterns():
            if pattern not in BandNamePattern.two_word_patterns():
                print(f"  - {pattern.value}")
        return 0

    # Create the band name generator instance
    generator = BandNameGenerator()

    # Convert pattern string to enum if specified, otherwise None for random
    pattern: BandNamePattern | None = None
    if args.pattern:
        # Convert the string value (e.g., "metal_noun") to enum
        pattern = BandNamePattern(args.pattern)

    # Handle random continuous mode
    if args.random:
        # In random mode: None means infinite, otherwise use specified count
        count = args.count if args.count is not None else 0
        return run_random_mode(generator, pattern, count, args.interval)

    # For normal mode: default to 1 if count not specified
    count = args.count if args.count is not None else 1

    # Generate the requested number of band names
    names = generator.generate(pattern=pattern, count=count)

    # Display results with appropriate formatting
    print()
    if count == 1:
        # Single name: simpler output format
        print("Generated band name:")
        print(f"  {names[0]}")
    else:
        # Multiple names: numbered list format
        print(f"Generated {count} band names:")
        for i, name in enumerate(names, 1):
            print(f"  {i}. {name}")
    print()

    return 0


def run_random_mode(
    generator: BandNameGenerator,
    pattern: BandNamePattern | None,
    count: int,
    interval: float,
) -> int:
    """Run continuous random mode generating names with pauses.

    Generates band names indefinitely (or up to count if specified) with
    a pause between each one. User can press Ctrl+C to exit gracefully.

    Args:
        generator: BandNameGenerator instance to use
        pattern: Optional pattern to use, None for random
        count: Number of names to generate (0 or negative for infinite)
        interval: Seconds to pause between names

    Returns:
        Exit code (0 for success, 1 for error)
    """
    # Set up signal handler for graceful Ctrl+C exit
    def signal_handler(sig, frame):
        print("\n\nRandom mode stopped by user.")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    # Print header
    print("\nRandom Band Name Generator")
    if count > 0:
        print(f"Generating {count} names with {interval}s intervals [Press Ctrl+C to stop]\n")
    else:
        print(f"Generating names continuously with {interval}s intervals [Press Ctrl+C to stop]\n")

    # Generate names in a loop
    iteration = 0
    while True:
        iteration += 1

        # Generate one name
        names = generator.generate(pattern=pattern, count=1)

        # Display the name
        print("Generated band name:")
        print(f"  {names[0]}")
        print()

        # Check if we've reached the count limit
        if count > 0 and iteration >= count:
            print(f"Generated {count} names. Exiting.")
            break

        # Pause before next iteration
        try:
            time.sleep(interval)
        except KeyboardInterrupt:
            print("\n\nRandom mode stopped by user.")
            return 0

    return 0
