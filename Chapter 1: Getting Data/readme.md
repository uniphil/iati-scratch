
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
