# Ticket and PR drafts

Drafts for upstreaming the migration optimizer work on the
`claude/zen-gauss-0iysjk` branch of https://github.com/adamchainz/django.

This directory is for coordination only and must not be included in any
upstream PR.

## New Trac tickets

Each `.trac.txt` file starts with the ticket form fields, then a
`Description` section written in Trac wiki formatting, ready to paste into
https://code.djangoproject.com/newticket.

Ticket #34534 was closed with a request for a new ticket per additional
reduction, so each reduction has its own ticket.

| File | Type | Branch commit |
|---|---|---|
| `01-addindex-reduce-model-name.trac.txt` | Bug | `ad36c0f2c` |
| `02-renameindex-removeindex.trac.txt` | Cleanup/optimization | `308d91cca` |
| `03-renameindex-undo.trac.txt` | Cleanup/optimization | `d336c8232` |
| `04-createmodel-renameindex.trac.txt` | Cleanup/optimization | `8489cef01` |
| `05-index-operations-deletemodel.trac.txt` | Cleanup/optimization | `b79fab8a2` |
| `06-renamemodel-undo.trac.txt` | Cleanup/optimization | `565f4f3d4` |
| `07-unique-field-fk-removal-order.trac.txt` | Bug | none (not fixed) |
| `08-constraint-index-referenced-fields.trac.txt` | New feature | none (proposal) |

After filing, reword each branch commit's message to start with
`Fixed #NNNNN -- `.

## Existing ticket #37151 and PR django/django#21442

The branch commits `73ed41b2c` and `01edd668d` duplicate the open ticket
#37151 and its PR, so they go there instead of to a new ticket:

- `37151/trac-comment.txt` – comment for the Trac ticket.
- `37151/pr-21442-comment.md` – comment for the GitHub PR.
- `37151/pr-21442-removeconstraint.patch` – a `fixup!` commit that applies
  with `git am` on top of the PR head `0f1dbccd0`. It fixes a foreign key
  ordering bug in the PR.

File ticket 07 first, then replace `#NNNNN` in `37151/trac-comment.txt`
with its number.
