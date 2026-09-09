# Springfield Training Center — Shopify Theme

Built on [Shopify Dawn](https://github.com/Shopify/dawn), restyled and extended with custom
sections/pages for Springfield Training Center (STC): a membership-acquisition website with a
small merchandise store.

## Connect this repo to your Shopify store

1. In Shopify admin: **Online Store → Themes → Add theme → Connect from GitHub**
2. Choose this repository (`petegeldes/springfield-training-center-theme`), branch `main`
3. This creates a new, **unpublished** theme — nothing goes live until you click Publish

## One-time setup in Shopify admin (do this after connecting)

### 1. Create pages
Go to **Online Store → Pages → Add page** for each of these, and set the page's **Template**
(right sidebar → Theme template) to match:

| Page title  | Handle (URL)     | Template            |
|-------------|------------------|----------------------|
| Memberships | `memberships`    | `page.memberships`  |
| Training    | `training`       | `page.training`      |
| Join        | `join`           | `page.join`          |
| Free Week   | `free-week`      | `page.free-week`     |
| Welcome     | `welcome`        | `page.welcome`       |

### 2. Set up navigation
**Online Store → Navigation**:
- Edit **Main menu**: Home (`/`), Memberships (`/pages/memberships`), Training (`/pages/training`),
  Shop (`/collections/all`), Join Now (`/pages/join`)
- Edit **Footer menu**: same links, minus Join Now if you'd rather keep it short

### 3. Upload the logo
**Theme editor → Theme settings → Logo**. Use `assets/stc-logo-small-light.png` from this repo
(a code-recreated version of your logo sheet — swap in your real vector/PNG files any time).

### 4. Add your Square Payment Links
Each membership plan button currently links to `#`. In the theme editor, open the **Memberships**
block on the homepage, the Training page, and the Join page, and paste in the real Square Payment
Link URL for each plan under **Button link**.

### 5. Fill in the placeholders
Search the theme editor for these and replace with real information:
- Phone number and email (footer, Location section)
- Zip code (Location section, and `layout/theme.liquid` LocalBusiness schema)
- Key pickup instructions (Welcome page)
- Membership waiver confirmation (Join page note)
- Real reviews (Testimonials section on the homepage — currently placeholders, clearly marked)
- Student/Family membership eligibility rules, if any

### 6. Connect your domain (when ready to go live)
**Settings → Domains** — point `springfieldtrainingcenter.com` at this store. This is a DNS
change; do it only when you're ready, since it affects your live site.

## What's real vs. what needs your input

**Already working:**
- All pages, copy, and pricing from the approved design
- 14 real photos from your gym, optimized and included as theme assets
- Free Week lead form — submits to Shopify's native contact form (arrives as an email
  notification; no third-party tool needed)
- Homepage "Shop STC" and the Shop page use Shopify's real product/collection system —
  add products normally and they'll appear automatically

**Needs your input before launch:** Square Payment Links, phone/email, zip code, key-pickup
instructions, waiver text, real testimonials — see the checklist above.
