# wearwise — functional UCD research prototype

**Version:** 1.0 · 26 November 2026

A mobile-first, high-fidelity reconstruction of the supplied `Video.mov` (2 min 24 sec) and the supporting `Copy of Design.pdf`. The video takes precedence over earlier sketches. This is a research prototype, not a live marketplace or an installed browser extension.

## Run the prototype

### Quick start (no installation)
1. Open `Wearwise_Prototype.html` in Chrome, Edge or another modern browser. The HTML contains the application, styles and all product photographs.
2. Choose **Create account** using the prefilled sample details, then select shopping-assistant priorities and finish setup.
3. To access the simulated extension and daily outfit notification, go to **You → See it in action**. The icon next to the wearwise logo also opens the shopping-assistant preview.

### Edit the source in VS Code (recommended for the project submission)
1. Extract this ZIP into a folder, then open that folder in VS Code.
2. In the VS Code terminal, run `python -m http.server 8000` (on Windows, use `py -m http.server 8000` if needed).
3. Open `http://localhost:8000` in a browser. Stop the server with Ctrl+C when finished.
4. Edit `app.js` for the catalogue, interaction logic and screens; `styles.css` for the visual design; `index.html` for the entry point; `assets/` for imagery.
5. Run `python build.py` to regenerate the self-contained HTML version after any edits.

The implementation deliberately uses standard HTML, CSS and JavaScript instead of React, so no npm installation or framework setup is needed. There are no runtime third-party dependencies or network requests. A static web host can publish the `index.html`, `app.js`, `styles.css` and `assets/` folder together; no backend is necessary. No site has been deployed as part of this delivery. For a research link, upload the static project to a university-approved host. Use a fresh browser profile or reset the demo between participants.

## Screen map and functionality

| Screen / flow | Implementation |
|---|---|
| Create account | Local demo identity; no real account or email transmission |
| Set up your shopping assistant | Affordability, style, material composition, second-hand switches |
| How do you dress? | Multiple style choices, summary and setup completion |
| Shop | Two-column photo grid (requested redesign), text search, category chips, filter sheet |
| Filters | Category, materials, budget, verified/second-hand choices and listing source; live result count |
| Product detail | Price, reference price, delivery, condition, size, materials and sample Good On You panel for new products |
| Buy on source | Clearly labelled simulated retailer/listing handoff; no invented live listing URLs or payments |
| Saved | Save/remove items with heart feedback, wishlist total and reference-price savings |
| Wardrobe | Seven starter items, category filters, upload/camera chooser, item details and removal |
| Add to wardrobe | Actual local image upload and resizing, item details and basic even-background replacement where feasible |
| Inspo | Outfit cards from the wardrobe, keep/pass buttons and horizontal touch swipes, style/occasion/season filtering, newly uploaded item combinations |
| You | Preferences, notification controls, demo previews and reset |
| Shopping assistant preview | Mobile top-right image-based notification, strict matching, dismiss or view in app; separate wardrobe reminder |
| Morning outfit preview | Simulated 7:30 notification and sample weather; opens outfit inspiration |

## Design provenance

- Video: account flow (0–36s), marketplace and filters (39–60s), product detail/wishlist (63–75s), wardrobe and outfit inspiration (78–105s), preferences and notification demos (108–143s).
- Portfolio page 4: all five focus-group participants selected the grid homepage. The revised homepage is the intentional layout change.
- Portfolio pages 7, 10–11: product-page intervention, photo preview, top-right mobile notification, dismissible controls.
- Portfolio page 15: repair and maintenance removed from scope in favour of the marketplace, shopping assistant and wardrobe.
- Portfolio pages 24, 28–29: the colour palette, previous realistic-photo grid and refinement decisions.

Palette: app `#F2F2E7`, cream `#F5F5DC`, ink `#5C4033`, dusty pink `#905560`, green `#526D1B`, sage `#D6E0C1`, alerts `#CC5500`. The prototype retains the video labels Shop / Saved / Wardrobe / Inspo / You, editorial serif headings and original wearwise wording where readable. Small details and some sample catalogue metadata were reconstructed from the low-resolution recording. Product photos are generated illustrative assets; they are not photos of real listings. The separate coat photograph is cropped from the supplied design portfolio.

## Recommendation rules

When shopping for the sample linen shirt (£35.99 with free delivery), the preview evaluates the sample alternative (£18 + £3.49 delivery). Every enabled constraint must pass:

- **Affordability:** alternative total cost must be strictly lower than the original total cost, not equal.
- **Style:** at least one selected style must match the alternative's sample style tags.
- **Material Composition:** at least one selected material must match the alternative's known material.
- **Second-hand Options:** if off, second-hand alternatives are excluded; if on, both new verified-brand and resale options are eligible.
- **Browser notifications:** if off, no notification is displayed.
- **Dismissal:** users can close the notification without blocking the retailer or purchase journey. A preview-only reset control is provided for testing.

Enabled style/material groups combine with AND; alternatives inside one group combine with OR. The “Already own similar” scenario is a separate wardrobe-reuse reminder, not a product-for-purchase recommendation, and is explained as such. Preferences are updated immediately; Save preferences validates selections and confirms the saved settings.

## Data and limitations

The catalogue and brand ratings are fixed illustrative data, not live availability or verified current ratings. No claim should be made that a listing is actually purchasable at these prices. No real account, retailer integration, checkout, payment, browser extension, weather API, scheduled system notification, AI image search, AI wardrobe recognition or trained recommender is implemented. Image search asks participants to choose a relevant category after uploading a picture. Outfits use curated combinations plus simple rules for newly uploaded clothes; keep/pass is recorded locally. Background replacement is basic colour-based processing and not AI segmentation. The original reference video is low-resolution; wording and layout are faithfully reconstructed where legible rather than a pixel-perfect copy. The application is responsive, but the core UI is intentionally phone-sized.

All preferences, demo name/city, wishlist and uploaded wardrobe photos stay in browser localStorage when available. Email is not stored. If local storage is blocked, the application still works in memory for that session. Browser storage is not a secure database: use sample identities and non-sensitive images, obtain participant consent where required, and use **You → Sign out & reset demo** between sessions. The app does not collect research analytics or send data anywhere.

## Verification

The JavaScript passed syntax checking. An automated Chromium UI smoke test exercised account creation, toggles, styles, filtering, rating panel, save/remove flow, photo upload, outfit keep action, qualifying recommendation, notification dismissal and restoration, simulated source handoff, non-matching material suppression, wardrobe reminder, morning notification and reset without uncaught JavaScript errors. The restricted development browser could not navigate to local URLs; tests loaded the standalone HTML into a browser document and used an in-memory storage substitute. Real browser localStorage, hosting and device-specific compatibility should be confirmed before participant sessions. No full WCAG compliance or production-level security audit has been performed.

See `USER_RESEARCH.md` for suggested tasks and a short moderator checklist. See `tests/smoke.py` for the reproducible automated interaction test (requires Python Playwright and Chromium, but not required to use the app).
