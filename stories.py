"""The 19 November 2026 front page: story list, figures and provenance.

Every item below was reported on Thursday 19 November 2026 or is a scheduled
event of that day.  Claims carried from Wednesday 18 November are named in the
date-check band rather than presented as Thursday's news.
"""

DATA = {
    "paper": "The World in One Day",
    "date_lines": ["Thursday", "19 November 2026"],
    "standfirst": "Three nuclear powers meet in Shenzhen  ·  GTA VI ships  ·  "
                  "The largest IPO ever priced starts trading",
    "region_order": ["EUROPE", "THE AMERICAS", "ASIA-PACIFIC", "MIDDLE EAST",
                     "AFRICA", "OCEANIA", "WORLD"],
    "figures": [
        ("$81.3bn", "raised by Anthropic, the largest IPO on record"),
        ("45%", "of Russia's refining offline after drone strikes"),
        ("50,000", "evacuated in Odisha as Cyclone Akvan nears"),
        ("4,595", "killed by armed violence in Haiti this year"),
        ("35 min", "of grounded flights across South Korea"),
        ("M5.7", "quake shakes Kumamoto before dawn"),
    ],
    "brief_header": "Also on Thursday 19 November",
    "date_check": (
        "reported on Wednesday 18 November, so not carried here as Thursday's news: "
        "Iran's drone strike on Ali Al-Salem air base in Kuwait and its attacks in Bahrain; "
        "the House Democrats' nomination of Hakeem Jeffries; Nvidia's halt of AI chip "
        "shipments to China; Brazil's Senate passing the fiscal package; Van Gogh's "
        "$190.4m sale at Sotheby's; Voyager 1 reaching one light-day at 05:16 ET."
    ),
    "footer": (
        "Every item above was reported, or happened, on Thursday 19 November 2026. "
        "Disputed claims are attributed to whoever made them. Counts on this page are "
        "computed from the stories themselves. Sources: AP, Reuters, Xinhua, Kyodo, "
        "The Hindu, BBC, ICJ, IMD, UN OCHA, Save the Children."
    ),
    "stories": [
        # ---------------- leads, illustrated ----------------
        dict(n=1, region="ASIA-PACIFIC", where="Shenzhen", art="flags",
             caption="Three flags, one table: the APEC leaders\' session in Shenzhen",
             head="Trump, Xi and Putin sit down together for the first time",
             text="The leaders of the three nuclear powers open a trilateral at APEC, "
                  "with arms control, the Iran war and Ukraine on the table. Trump and "
                  "Putin held a bilateral first, officials said.",
             lon=114.06, lat=22.54),
        dict(n=2, region="THE AMERICAS", where="New York", art="skyline",
             caption="Launch night in a city Rockstar has spent 13 years rebuilding",
             head="GTA VI ships at midnight, thirteen years after GTA V",
             text="Rockstar's sequel unlocks in each time zone in turn, New Zealand "
                  "first. No PC version yet. Retailers reported a rush on leave requests "
                  "for launch week.",
             lon=-74.0, lat=40.71),
        dict(n=3, region="THE AMERICAS", where="Nasdaq", art="candles",
             caption="First-day trading in Anthropic, the biggest listing on record",
             head="Anthropic begins trading after the largest IPO ever priced",
             text="Priced at $83 a share, above its range, the Claude maker raised "
                  "$81.3bn. The first trades set the real price; up to a fifth of the "
                  "offering went to retail buyers.",
             lon=-73.99, lat=40.75),

        # ---------------- mid grid ----------------
        dict(n=4, region="EUROPE", where="The Hague", mid=True,
             head="World Court reads its Rohingya judgment",
             text="The ICJ delivers judgment in The Gambia's case against Myanmar over "
                  "the 2017 campaign. The reading began at 10:00 local.",
             lon=4.3, lat=52.08),
        dict(n=5, region="EUROPE", where="Antalya", mid=True,
             head="COP31 enters its last two days with finance unresolved",
             text="Ministers take over the text. A draft targets $120bn a year of "
                  "adaptation finance by 2035; how to pay for it is still open.",
             lon=30.7, lat=36.9),
        dict(n=6, region="ASIA-PACIFIC", where="Odisha", mid=True,
             head="50,000 evacuated as Cyclone Akvan closes on the coast",
             text="Red alerts across coastal districts; landfall forecast for Friday "
                  "between Narsapur and Puri. Andhra Pradesh and West Bengal are on "
                  "alert too.",
             lon=85.8, lat=20.3),
        dict(n=7, region="ASIA-PACIFIC", where="Seoul", mid=True,
             head="Korea halts every flight for the exam's listening test",
             text="All take-offs and landings pause for 35 minutes and the stock market "
                  "opens late, as 500,000-odd candidates sit the suneung.",
             lon=126.98, lat=37.57),
        dict(n=8, region="EUROPE", where="Kyiv", mid=True,
             head="The Kerch bridge is hit again, Russian officials say",
             text="Traffic halted on the Crimea bridge after an attack; Russia's embassy "
                  "in the Netherlands asked whether Dutch-supplied drones were used.",
             lon=30.52, lat=50.45),
        dict(n=9, region="ASIA-PACIFIC", where="Dhaka", mid=True,
             head="Four killed as a shutdown called by Hasina's party grips Bangladesh",
             text="Protests close parts of the country and a fire, suspected arson, "
                  "damages Muhammad Yunus's ancestral home in Chattogram.",
             lon=90.4, lat=23.81),
        dict(n=10, region="AFRICA", where="Nairobi", mid=True,
             head="Kenya's flood death toll reaches 71 as the rains go on",
             text="Flash floods have displaced thousands; Nairobi has recorded the most "
                  "deaths of any county, police figures show.",
             lon=36.82, lat=-1.29),
        dict(n=11, region="ASIA-PACIFIC", where="Kumamoto", mid=True,
             head="Magnitude 5.7 quake shakes Kyushu before dawn",
             text="The 02:22 temblor struck at a depth of about 10km in the "
                  "Amakusa-Ashikita area. No tsunami warning was issued.",
             lon=130.7, lat=32.79),
        dict(n=12, region="OCEANIA", where="Wellington", mid=True,
             head="Nicholls hundred answers Bumrah on the first day",
             text="New Zealand recovered from 70 for 5 at the Basin Reserve after "
                  "Jasprit Bumrah's opening burst; Henry Nicholls made his 12th Test ton.",
             lon=174.78, lat=-41.29),
        dict(n=13, region="WORLD", where="Geneva", mid=True,
             head="Nearly one child in four now lives in a conflict zone",
             text="Save the Children puts the number at a record high, with 14,224 "
                  "children killed or maimed in conflicts during 2025.",
             lon=6.14, lat=46.2),
        dict(n=14, region="EUROPE", where="London", mid=True,
             head="Sotheby's confirms the Van Gogh record stands",
             text="The chestnut-tree canvas made $190.4m with fees on Wednesday night "
                  "after an 11th-hour settlement with the heirs of its former owner.",
             lon=-0.13, lat=51.51),

        # ---------------- briefs ----------------
        dict(n=15, region="MIDDLE EAST", where="Riyadh",
             head="Gulf states ask Trump to hold off on further strikes on Iran",
             lon=46.72, lat=24.71),
        dict(n=16, region="MIDDLE EAST", where="Tehran",
             head="Iran says it still awaits the American reply to its Hormuz proposal",
             lon=51.39, lat=35.69),
        dict(n=17, region="MIDDLE EAST", where="Dubai",
             head="ADNOC reports a crew member missing after its vessel was hit in Hormuz",
             lon=55.27, lat=25.2),
        dict(n=18, region="MIDDLE EAST", where="Baghdad",
             head="Six French ISIL members sentenced to life by an Iraqi court",
             lon=44.36, lat=33.31),
        dict(n=19, region="MIDDLE EAST", where="Beirut",
             head="Eighty-four Syrian refugees return from Lebanon in an organised convoy",
             lon=35.5, lat=33.89),
        dict(n=20, region="ASIA-PACIFIC", where="Tokyo",
             head="Takaichi and Xi shake hands at APEC as ties stay frosty",
             lon=139.69, lat=35.69),
        dict(n=21, region="ASIA-PACIFIC", where="New Delhi",
             head="India and Canada near a defence pact for Modi's December visit",
             lon=77.21, lat=28.61),
        dict(n=22, region="ASIA-PACIFIC", where="Bengaluru",
             head="Amazon pledges $7bn for robotics in India by 2030",
             lon=77.59, lat=12.97),
        dict(n=23, region="ASIA-PACIFIC", where="Beijing",
             head="Industrial output grew 4.8% in October, slower than September",
             lon=116.4, lat=39.9),
        dict(n=24, region="ASIA-PACIFIC", where="Jakarta",
             head="Governments warn a Java logging flaw leaves systems open to attack",
             lon=106.85, lat=-6.21),
        dict(n=25, region="ASIA-PACIFIC", where="Manila",
             head="ASEAN and its three northeast Asian partners press on with Manila agenda",
             lon=120.98, lat=14.6),
        dict(n=26, region="THE AMERICAS", where="Washington",
             head="Peltola's Alaska win confirmed, a Democratic Senate gain",
             lon=-77.04, lat=38.9),
        dict(n=27, region="THE AMERICAS", where="Caracas",
             head="Hegseth signs a military co-operation agreement with Venezuela",
             lon=-66.9, lat=10.49),
        dict(n=28, region="THE AMERICAS", where="Mexico City",
             head="Federal forces arrest a suspected leader of the Los Deltas cell",
             lon=-99.13, lat=19.43),
        dict(n=29, region="THE AMERICAS", where="Port-au-Prince",
             head="UN counts 4,595 killed in Haiti's gang violence this year",
             lon=-72.34, lat=18.54),
        dict(n=30, region="THE AMERICAS", where="Ottawa",
             head="Carney says Canada will widen China ties to win the right US deal",
             lon=-75.7, lat=45.42),
        dict(n=31, region="AFRICA", where="Khartoum",
             head="Sudan's army advances in West Kordofan as the RSF pulls back",
             lon=32.53, lat=15.5),
        dict(n=32, region="AFRICA", where="Mogadishu",
             head="Somalia's constitutional overhaul tests its federal bargain",
             lon=45.34, lat=2.05),
        dict(n=33, region="AFRICA", where="Brazzaville",
             head="Sassou-Nguesso opens a mediation between Tshisekedi and Ruto",
             lon=15.28, lat=-4.27),
        dict(n=34, region="AFRICA", where="Lungi",
             head="West African leaders sign four integration agreements",
             lon=-13.2, lat=8.6),
        dict(n=35, region="OCEANIA", where="Canberra",
             head="Australia sanctions three more settlers and four settler groups",
             lon=149.13, lat=-35.28),
        dict(n=36, region="OCEANIA", where="Sydney",
             head="Economists warn Australia is showing the hallmarks of a recession",
             lon=151.21, lat=-33.87),
        dict(n=37, region="OCEANIA", where="Port Vila",
             head="Vanuatu asks COP31 to reform the UN climate summit process",
             lon=168.32, lat=-17.73),
        dict(n=38, region="EUROPE", where="Paris",
             head="Ministers try to unblock the COP31 text before the gavel",
             lon=2.35, lat=48.86),
        dict(n=39, region="EUROPE", where="Brussels",
             head="The EU's proposed €45bn loan for Ukraine awaits a decision",
             lon=4.35, lat=50.85),
        dict(n=40, region="EUROPE", where="Amsterdam",
             head="Europe's scrap exporters fight over the future of waste shipments",
             lon=4.9, lat=52.37),
        dict(n=41, region="EUROPE", where="Moscow",
             head="Drone strikes have nearly halved Russia's November refining",
             lon=37.62, lat=55.75),
        dict(n=42, region="WORLD", where="Geneva",
             head="The UN warns anti-gang operations in Haiti must spare civilians",
             lon=6.15, lat=46.21),
        dict(n=43, region="WORLD", where="Bangkok",
             head="Reproductive genetics conference closes with a call for translation",
             lon=100.5, lat=13.75),
        dict(n=44, region="WORLD", where="Shenzhen",
             head="APEC chief executives issue the Shenzhen Initiative on growth",
             lon=114.07, lat=22.55),
    ],
}
