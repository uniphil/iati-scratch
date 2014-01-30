
Getting Data
============

The first thing I wanted to do was explore the process of getting IATI data.
I'm interested in this experience for users, so I'm skipping the wonderful APIs
available and scraping web pages instead.

IATI data is published on publishers' websites. There is no central "correct"
source for the data, though there is a [registry](http://www.iatiregistry.org).

I spent a while clicking around on the registry site looking for the links
pointing off-site to the original source. I kept skipping over all of links
that said "Download", thinking they were registry-hosted files. This was quite
frustrating.

### Idea #1: Re-label `Download` buttons in the registry to `Download from
:source`. So say, `Download from AidStream` for the registry file links.


Distraction: Getting Emails
---------------------------

**script:** [who_publishes.py](who_publishes.py)

Since I (thought I) couldn't find any external links, I started scraping the
dataset pages and pulling email addresses. Most Datasets have this in the
contact-info box on the right, and most email accounts seem to be on the domain
of the publishing organization, so I took this as a messy way to link up to
publishing organization websites.

Here is the output of `python who_publishes.py` for as of January 30th:
```
REPORT

Some numbers:
 * 242 publishers
 * 128 email addresses
 * 665 datasets

Datasets with no provided email address:
 * 19 datasets from European Commission – Development and Cooperation-EuropeAid
 * 19 datasets from Finland, Ministry of Foreign Affairs
 * 19 datasets from United States
 * 19 datasets from Asian Development Bank
 * 10 datasets from European Commission - Enlargement
 * 19 datasets from European Commission – Service for Foreign Policy Instruments

Publishers providing multiple email addresses:
 * Agency for cooperation and research in development:
    1 datasets from vanessa.dupont@acordinternatio
    1 datasets from nicola.bevan@acordinternational.org
 * Christian Aid:
    2 datasets from info@christian-aid.org
    1 datasets from HCook@christian-aid.org
    1 datasets from hcook@christian-aid.org
 * Concern Worldwide UK:
    1 datasets from bob.ruxton@concern.net
    1 datasets from natalie.pedersen@concern.net
 * Homeless International:
    4 datasets from remi@homeless-international.org
    1 datasets from remi@homeless-international.or
 * HTSPE:
    1 datasets from keith.smith@htspe.com
    1 datasets from info@htspe.com
 * Tearfund:
    2 datasets from andrew.watt@tearfund.org
    2 datasets from jessica.malcolm@tearfund.org
 * Transparency International Secretariat:
    5 datasets from garnaudo@transparency.org
    6 datasets from sbley@transparency.org
 * WWF-UK:
    1 datasets from wbeale@wwf,org,uk
    6 datasets from wbeale@wwf.org.uk

Sketchy email addresses:
 * WWF-UK
    wbeale@wwf,org,uk
 * African Initiatives
    dermot.byron1@gmail.com
 * Zimbabwe Educational Trust
    stuartkempster@hotmail.com
 * Association for Reproductive and Family Health 
    enejoamade@gmail.com
```

The data scraped for this report is tracked in [results.json](results.json).

