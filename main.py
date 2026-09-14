import argparse
import asyncio
from database.schema import initialise_database


def parse_args():
    parser = argparse.ArgumentParser(description="Local Job Matching Agent")
    parser.add_argument("--location", default="London")
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--minimum-score", type=float, default=7)
    parser.add_argument("--limit", type=int, default=10)
    return parser.parse_args()


async def run(args):
    initialise_database()
    print("Local Job Matching Agent")
    print(f"Location: {args.location}")
    print(f"Time window: {args.hours} hours")
    print(f"Minimum score: {args.minimum_score}")
    print(f"Result limit: {args.limit}")
    print()
    print("Database initialised.")
    print("End-to-end collectors and scoring are the next implementation stage.")


if __name__ == "__main__":
    asyncio.run(run(parse_args()))
