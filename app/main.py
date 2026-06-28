from app.graph.graph import build_graph


def create_initial_state() -> dict:
    return {
        "run_date": "",
        "market_data": {},
        "rates_data": {},
        "macro_data": {},
        "central_bank_data": {},
        "news_data": {},
        "warnings": [],
        "draft_brief": "",
        "final_brief": "",
        "sources": [],
    }


def main() -> None:
    app = build_graph()
    result = app.invoke(create_initial_state())

    print("\n" + "=" * 80)
    print(result["final_brief"])
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()