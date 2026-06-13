# === Stage 16: Add argparse support for the most common commands ===
# Project: CraftFlow
import argparse

def main():
    parser = argparse.ArgumentParser(description="CraftFlow: Creative Project Tracker")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add project command
    proj_parser = subparsers.add_parser('add-project', help='Add a new creative project')
    proj_parser.add_argument('--name', required=True, help='Project name')
    proj_parser.add_argument('--category', default='general', help='Category (e.g., woodwork, digital)')

    # Add material command
    mat_parser = subparsers.add_parser('add-material', help='Add a project material')
    mat_parser.add_argument('--project', required=True, help='Project name or ID')
    mat_parser.add_argument('--item', required=True, help='Material item (e.g., oak wood)')
    mat_parser.add_argument('--cost', type=float, default=0.0, help='Cost in local currency')

    # Add milestone command
    mil_parser = subparsers.add_parser('add-milestone', help='Add a project milestone')
    mil_parser.add_argument('--project', required=True, help='Project name or ID')
    mil_parser.add_argument('--title', required=True, help='Milestone title')
    mil_parser.add_argument('--date', default=None, help='Target date (YYYY-MM-DD)')

    # Add inspiration command
    insp_parser = subparsers.add_parser('add-inspiration', help='Add an inspiration note')
    insp_parser.add_argument('--project', required=True, help='Project name or ID')
    insp_parser.add_argument('--note', required=True, help='Inspiration text')

    args = parser.parse_args()
    if not hasattr(args, 'command'):
        parser.print_help()
        return 1
    
    # Placeholder for actual logic implementation based on parsed arguments
    print(f"Executing command: {args.command}")
    
    if args.command == 'add-project':
        print(f"Project '{args.name}' added to category '{args.category}'.")
    elif args.command == 'add-material':
        print(f"Material '{args.item}' for project '{args.project}' recorded with cost {args.cost}.")
    elif args.command == 'add-milestone':
        print(f"Milestone '{args.title}' scheduled for {args.date} in project '{args.project}'.")
    elif args.command == 'add-inspiration':
        print(f"Inspiration note added to project '{args.project}'.")

if __name__ == "__main__":
    main()
