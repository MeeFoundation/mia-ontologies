### Context File Naming Convention

Context DataBook filenames used in the Alice Walker example follow the pattern:

```
<subject>.<claimant>(<containing-category>)(<NN>).databook.md
```

| Segment | Meaning |
|---|---|
| `<subject>` | Who the context is about. `self` when the subject is the Mia user (`:Self`); the full hyphenated lowercase name otherwise (e.g. `paula-walker`, `bob-johnson`, `bhs-group`). |
| `<claimant>` | Who recorded the data. `self` when the claimant is `:Self`; the full hyphenated lowercase name otherwise (e.g. `bob-johnson`, `citibank`); the literal `members` for group contexts where any member may write. |
| `(<containing-category>)` | The filename root of the category DataBook that directly holds the `obs`, `sbs`, `obo`, or `sbo` link pointing to this context (e.g. `(paula-walker)`, `(bob-johnson)`, `(boston-hub-society)`, `(acme)`, `(citibank)`). This is often a user-defined category DataBook — it is NOT the `mia.category` IRI local name of the canonical category. |
| `(<NN>)` | Zero-padded two-digit context number in parentheses. |

The document IRI uses the same local name under the `https://www.example.org/mia/contexts/` base. For example, `self.citibank(citibank)(09).databook.md` has `id: https://www.example.org/mia/contexts/self.citibank(citibank)(09)`.

Examples:

| File | Subject | Claimed by | Containing category DataBook |
|---|---|---|---|
| `self.self(paula-walker)(employee)(20).databook.md` | Self (Alice) | Self (Alice) | `paula-walker(acme).databook.md` |
| `paula-walker.self(paula-walker)(family)(07).databook.md` | Paula Walker | Self (Alice) | `paula-walker(family).databook.md` |
| `self.bob-johnson(bob-johnson)(08).databook.md` | Self (Alice) | Bob Johnson | `bob-johnson(people).databook.md` |
| `bob-johnson.bob-johnson(boston-hub-society)(03).databook.md` | Bob Johnson | Bob Johnson | `boston-hub-society(affiliations).databook.md` |
| `bhs-group.members(boston-hub-society)(01).databook.md` | BHS Group | members (group) | `boston-hub-society(affiliations).databook.md` |