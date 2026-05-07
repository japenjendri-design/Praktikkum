def hero(data):
    hunters = data["hunters"]
    elements = data["elements"]
    query = data["query"]

    # 1. Logika Rank Hunter
    if query.get("RANK_HUNTER"):
        print("=== RANK HUNTER ===")

        total = {}

        for hunter, info in hunters.items():
            total_power = sum(info["skills"].values())
            total[hunter] = total_power

        sorted_total = list(map(tuple, total.items()))

        for i, (hunter, power) in enumerate(sorted_total, start=1):
            print(f"#{i} {hunter} | Total Power: {power}")

    # 2. Logika Resonance
    if query.get("RESONANCE"):
        el = query.get("RESONANCE")
        print(f"\n=== RESONANCE: {el} ===")

        for hunter, info in hunters.items():
            for skill in info["skills"]:
                if el in elements.get(skill, ""):
                    print(f"{hunter}: {skill}")

    # 3. Logika Keamanan
    if query.get("RANK_HUNTER") == False and query.get("RESONANCE") is None:
        print("Analisis Terlarang. Kamu Tidak Bisa Mengakses File Ini")
