#!/usr/bin/env python3
"""Build the Viral Coach (Daniel Iles) swipe site.

A done-for-you social agency selling on a hard performance guarantee.
The move worth having is in the first ten seconds of the VSL.

Run: python3 build_site.py
"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/DANIEL_ILES_Swipe")

ROLES = {
    "ViralCoach_MainVSL.mp4": "The main-page VSL. Opens on the guarantee, then reframes off it.",
    "Application_Hero.mp4": "Long client-story reel running on the application page.",
    "Application_ProofLoop.mp4": "Second story reel, looped behind the proof grid.",
    "PreCall_ShowUpPrepared.mp4": "Thanks-page clip labelled &ldquo;watch this so you show up prepared&rdquo; &mdash; 10s, silent.",
}


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/*.mp4"))):
        b = os.path.basename(p)
        mb = os.path.getsize(p) / 1e6
        rows.append((b, _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     ROLES.get(b, "")))
    return rows


CONFIG = {
    "SITE": "Viral Coach — 1 Million Views Guaranteed",
    "CREATOR": "Daniel Iles",
    "ADS_KEY": "viralcoach",
    "FUNNEL_IDS": ["F036"],
    "CAPTURED": "30 July and 11 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/DANIEL_ILES_Swipe",
    "BLURB": "Done-for-you social media for local and professional businesses, sold on a hard "
             "performance guarantee &mdash; <b>one million views or you don't pay</b>. The whole "
             "funnel is three pages, and the sharpest move happens in the first ten seconds of "
             "the VSL.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("transcripts.html", "Transcripts"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("Company", "Viral Coach, LLC"),
        ("Model", "DFY agency retainer"),
        ("Guarantee", "1,000,000 views or you don't pay"),
        ("Funnel", "3 pages"),
        ("Clients claimed", "3,000+"),
        ("Niches claimed", "250+"),
        ("Price", "never stated"),
        ("Words captured", "7,483"),
    ],

    "OFFER": [
        ("Product", "Fully-managed social media &mdash; editing, positioning, paid, organic, distribution"),
        ("Promise", "&ldquo;Grow your business with social media. Fully-managed system with "
                    "<b>guaranteed performance</b>&rdquo;"),
        ("Guarantee", "<b>1,000,000 views or you don't pay.</b> Stated in the VSL's opening line "
                      "and repeated as the closing card on every page"),
        ("ICP", "Established local and professional businesses &mdash; plumbers, attorneys, "
                "dentists, contractors, clinicians. Not creators"),
        ("Proof claims", "15.5M average client views in 90 days · 3,000+ clients · 250+ niches · "
                         "4.8/5 G2 · 4.9/5 Clutch"),
        ("Path", "Main page &rarr; application (&ldquo;see if you qualify&rdquo;) &rarr; booked "
                 "call &rarr; thanks page with calendar add + pre-call clip"),
        ("Price", "<b>Never stated.</b> No figure appears on any captured page or in any of the "
                  "three transcripts"),
    ],

    "FINDINGS": [
        ("The VSL disowns its own hook in the first ten seconds &mdash; steal this",
         "It opens: <i>&ldquo;We'll get you a million views or you don't pay. <b>But</b> after "
         "working with thousands of business owners, we know what they're actually looking for is "
         "how to grow their business with all of that traffic.&rdquo;</i> The guarantee is what "
         "earns the click, so he leads with it &mdash; then immediately tells you it is not the "
         "point. He gets the credit for the bold promise <i>and</i> the credibility of being the "
         "one to say it is not what you really want. Our class opens by defending its own promise; "
         "this opens by moving past it."),
        ("Paid traffic never sees the main page",
         "<b>The Meta Pixel and GoHighLevel fire on the application page only.</b> The main page "
         "carries GTM, GA and Clarity &mdash; analytics, no ad tech. That is not an oversight on a "
         "site this tidy: the main page is the brand and organic destination, and paid traffic is "
         "pointed straight at <code>/application</code>. Two entry points, two jobs."),
        ("Every CTA is a qualification, never a booking",
         "The button says <b>SEE IF YOU QUALIFY</b>, not &ldquo;book a call&rdquo; or &ldquo;get "
         "started free&rdquo;. The page header is the same. It reframes the click from <i>asking "
         "them for time</i> to <i>submitting for judgement</i> &mdash; and it pre-loads the "
         "screening the call is going to do anyway."),
        ("Twelve named clients across twelve unrelated niches",
         "A plumber, a defense attorney, a fertility specialist, a myofunctional therapist, a "
         "hockey coach, an e-commerce operator. Each a named person with hard numbers. The grid "
         "does one job: <b>it kills &ldquo;that won't work in my industry&rdquo; before the "
         "objection forms.</b> Depth would be wasted here; the breadth <i>is</i> the argument. "
         "Directly relevant to us &mdash; our proof clusters in one niche shape."),
        ("The guarantee is on a metric they control",
         "Views, not revenue, not leads. They can buy and engineer views; they cannot control "
         "whether a client's business converts them. Same structure as Bill Von Fumetti "
         "guaranteeing you pass a certification rather than that you earn. <b>The bold promise is "
         "always on the operator's side of the line.</b>"),
        ("Nothing changed in twelve days",
         "The 30 July and 11 August captures are <b>byte-for-byte identical in visible text</b> "
         "across all three pages. Nothing is being split-tested at the page layer. Whatever they "
         "are optimising, it is upstream in the ads."),
    ],

    "FUNNEL": [
        ("Main page", "viralcoach.com",
         "Long-form Framer page. Stat bar, VSL, service grid, ~15 testimonials on a loop, FAQ. "
         "GTM + GA + Clarity, <b>no Meta Pixel</b>."),
        ("Application", "viralcoach.com/application",
         '<span class="tag good">the paid entry point</span> &ldquo;SEE IF YOU QUALIFY&rdquo;. '
         'Twelve-card proof grid, two long story reels. <b>Meta Pixel + GoHighLevel fire here.</b>'),
        ("Thanks / booked", "viralcoach.com/thanks",
         "Add to Google Calendar / iCal, plus a clip captioned &ldquo;watch this so you show up "
         "prepared&rdquo;. Recording-consent notice for the call."),
    ],

    "TRANSCRIPT_GROUPS": [
        ("Main page VSL", [os.path.join(PKG, "Transcript/transcript.md")]),
        ("Application page reels", sorted(glob.glob(os.path.join(PKG, "Transcript/*_transcript.md")))),
    ],

    "SLIDE_PAGES": [],
    "VIDEOS": video_library(),

    "ANALYSIS": """
<div class="note"><b>One move here is worth the whole capture.</b> The VSL leads with the
guarantee that earned the click and then tells you, ten seconds in, that the guarantee is not
what you actually want. It is the cleanest hook-to-reframe transition in this swipe file.</div>

<h2 class="sec">The opening, line by line</h2>
<div class="tablewrap"><table>
<tr><th>What he says</th><th>What it does</th></tr>
<tr><td>&ldquo;We'll get you a million views or you don't pay.&rdquo;</td>
    <td>Pays off the ad instantly. No throat-clear, no &ldquo;hi, I'm Daniel&rdquo;.</td></tr>
<tr><td>&ldquo;<b>But</b> after working with thousands of business owners&hellip;&rdquo;</td>
    <td>Volume as the right to reframe. He is not guessing, he has seen it.</td></tr>
<tr><td>&ldquo;&hellip;what they're <b>actually</b> looking for is how to grow their business.&rdquo;</td>
    <td>Names the real desire and makes the headline promise the lesser one.</td></tr>
<tr><td>&ldquo;That is what we really specialize in.&rdquo;</td>
    <td>Re-anchors the offer on the bigger thing, which now cannot be compared on price.</td></tr>
</table></div>
<p style="margin-top:12px">The trap he avoids is worth naming. Most VSLs that open on a bold
guarantee spend the next two minutes <i>defending</i> it &mdash; proof, mechanism, why it is
credible. Defending keeps the conversation on the guarantee, where the prospect is a sceptic.
He moves the conversation somewhere the prospect is a believer instead.</p>

<h2 class="sec">Two entry points, two tracking stacks</h2>
<div class="tablewrap"><table>
<tr><th>Page</th><th>Trackers</th><th>Read</th></tr>
<tr><td>Main page</td><td>GTM, GA, Clarity</td><td>Organic / brand / direct</td></tr>
<tr><td><b>Application</b></td><td>GTM, GA, Clarity, <b>Meta Pixel</b>, <b>GoHighLevel</b></td>
    <td><b>The paid destination.</b> Ads land here, not on the main page</td></tr>
<tr><td>Thanks</td><td>GTM, GA, Clarity</td><td>Conversion fires from the app page, not here</td></tr>
</table></div>
<p style="margin-top:12px"><span class="tag">READ</span> They run a page whose only job is to
convert cold paid traffic, and a separate page whose job is to be the company. We collapse those
into one. Worth asking whether our class registration page is being asked to do both jobs at once.</p>
<p><span class="tag">EVIDENCE</span> They are on <b>GoHighLevel</b>, same as us.</p>

<h2 class="sec">The proof grid is breadth, deliberately</h2>
<p>Twelve cards, twelve named clients, twelve unrelated industries &mdash; Jered the plumber
(427k followers, replaced $60k/mo in ad spend), Adam the defense attorney (344 &rarr; 230k
followers, 39.1M views), Greg the fertility specialist ($377 spent, $96,000 closed), Chelcie the
myofunctional therapist. No two share a market.</p>
<p>For an agency selling to <i>every</i> local business, the killer objection is &ldquo;my
industry is different.&rdquo; A deep case study in one niche makes that objection worse. Twelve
shallow ones across twelve niches make it unaskable. <b>The structure of the proof is doing the
persuasion, not the content of any single card.</b></p>
<p><span class="tag">READ</span> Ours runs the other way &mdash; deep proof, narrow shape. That
is right while we sell one avatar and wrong the moment we widen. Something to hold.</p>

<h2 class="sec">What is missing, and stays missing</h2>
<ul>
<li><b>No price, anywhere.</b> Not on a page, not in 7,483 transcribed words. It lives on the call.</li>
<li><b>No email sequence.</b> The opt-in was never submitted, so nothing has been received. This is
the one real gap in this capture.</li>
<li><b>The pre-call video does not resolve.</b> The thanks page says &ldquo;watch this video so you
can show up prepared&rdquo;, but the only asset on it is a <b>10-second silent clip</b>. Either the
real video is gated behind the booking, or the label is decoration. Recorded as unresolved rather
than guessed at.</li>
<li><b>No ads pulled yet.</b> Meta fires on the application page, so a library almost certainly
exists.</li>
</ul>

<h2 class="sec">Where this sits against the rest of the file</h2>
<div class="tablewrap"><table>
<tr><th>Who</th><th>Guarantee is on&hellip;</th><th>Controlled by</th></tr>
<tr><td><b>Viral Coach</b></td><td>1,000,000 views</td><td><b>Them</b></td></tr>
<tr><td>Bill Von Fumetti</td><td>You pass the QuickBooks certifications</td><td><b>Them</b></td></tr>
<tr><td>John Madsen (Suprahuman)</td><td>Your physical result, or money back</td><td>Shared</td></tr>
</table></div>
<p style="margin-top:12px">Three unrelated markets, one shape: <b>the guarantee is always written
on an outcome the seller can force.</b> Nobody guarantees the buyer's revenue.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
