from app.graph.state import InstitutionalBriefState


def write_brief(state: InstitutionalBriefState) -> InstitutionalBriefState:
    """
    Mock institutional brief writer for Sprint 1.
    No LLM call yet.
    """

    market_data = state["market_data"]
    rates_data = state["rates_data"]
    macro_data = state["macro_data"]
    central_bank_data = state["central_bank_data"]
    news_data = state["news_data"]

    brief = f"""
Point institutionnel quotidien — {state["run_date"]}

1. Synthèse exécutive
Les marchés actions évoluent de manière contrastée dans ce jeu de données de test. Les investisseurs restent attentifs aux anticipations de politique monétaire et aux prochains indicateurs macroéconomiques.

2. Marchés actions
S&P 500 : {market_data["equities"]["S&P 500"]["daily_change_pct"]}%
Nasdaq : {market_data["equities"]["Nasdaq"]["daily_change_pct"]}%
Euro Stoxx 50 : {market_data["equities"]["Euro Stoxx 50"]["daily_change_pct"]}%
CAC 40 : {market_data["equities"]["CAC 40"]["daily_change_pct"]}%

3. Taux
US 2Y : {rates_data["US 2Y"]["yield_pct"]}% ({rates_data["US 2Y"]["daily_change_bps"]} bps)
US 10Y : {rates_data["US 10Y"]["yield_pct"]}% ({rates_data["US 10Y"]["daily_change_bps"]} bps)
Bund 10Y : {rates_data["EUR 10Y Bund"]["yield_pct"]}% ({rates_data["EUR 10Y Bund"]["daily_change_bps"]} bps)

4. Macro / banques centrales
Calendrier macro du jour : {", ".join(macro_data["today_calendar"])}
Fed : {central_bank_data["fed"]}
BCE : {central_bank_data["ecb"]}

5. News
- {news_data["headlines"][0]}
- {news_data["headlines"][1]}

6. Sources
- {state["sources"][0]["name"]} : {state["sources"][0]["url"]}
""".strip()

    state["draft_brief"] = brief
    state["final_brief"] = brief

    return state