This module restricts access to fields

* email
* phone
* mobile
* address
* birthdate_date

to users of group "Access to Private Addresses".

This module hides these fields from views of modules

- base
- mail

These modules were checked as well :

- account
- event
- payment
- purchase
- sale
- sms

- account_customer_wallet
- beesdoo_website_shift
- eater
- eater_member_card
- l10n_fr_siret
- member_card
- partner_firstname
- partner_contact_birthdate
- partner_contact_gender
- product_origin
- purchase_triple_discount
- recurring_consignment

We could not restrict fields access at model level because it breaks views throughout.
