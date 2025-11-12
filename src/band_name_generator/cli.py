"""Command-line interface for band name generator.

This module provides the CLI for generating band names with various patterns.
Users can generate random names, specify patterns, and control the number of
names generated.

Usage:
    python -m band_name_generator                    # Generate 1 random name
    python -m band_name_generator -n 10              # Generate 10 names
    python -m band_name_generator -p metal_noun      # Use specific pattern
    python -m band_name_generator -l                 # List available patterns
"""

import argparse

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
        default=1,
        help="Number of band names to generate (default: 1)",
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

    # Generate the requested number of band names
    names = generator.generate(pattern=pattern, count=args.count)

    # Display results with appropriate formatting
    print()
    if args.count == 1:
        # Single name: simpler output format
        print("Generated band name:")
        print(f"  {names[0]}")
    else:
        # Multiple names: numbered list format
        print(f"Generated {args.count} band names:")
        for i, name in enumerate(names, 1):
            print(f"  {i}. {name}")
    print()

    return 0
