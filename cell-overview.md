A cell is a secure **container of information** stored on the user’s devices. Each cell is created and managed by the Mia software application. A cell can be shared with one or more other members. These other members are usually other users, but may also be organizations that are compatible with the Personal Data Network.

The app contains two pre-defined tree structures of **categories**. These categories are “template” cells which may contain some starter content. They may also have a specific schema for the structured information that the cell can contain. Most cells are instantiated from a “template” cell from the category tree, although the user is allowed to create category-less cells if desired.

A cell has a **name**. Often this name is just a copy of the name of the category. For example if the category was "People”, the cell might be called “People”. However, the user can override this string with their own name. 

A cell has an **origin**. The origin is just the category (e.g. “People”) whose associated template cell was cloned to create the cell.

A cell has a **creator**, which is identity of the user who created it. 

A cell can be **shared**. The creator of a cell can invite people (or organizations compatible with the Mee Personal Data Network protocols) to join the cell. When they do they get a complete copy of the cell that is “alive”—any changes made to its contents are continuously shared with all members.

A cell is a container, so can be empty, or it can contain various kinds of information. The app displays different kinds of information in a cell in different tabs in the UI:

* **Info** tab: 
  * Structured information organized into one or more **topics**. 
  * Some topics are about members of the cell. A cell when created has one member (the creator). 
  * A cell may also have one “other” topic which can be about anything else (e.g. medications for a cat that the cell members are taking care of). 
  * Each topic has a *subject* and a *claimant*. The subject is typically a person, organization, or group, but it could be any other entity the Persona ontology can describe. The claimant is the person, group or organization that is asserting the values of the claims in the topic.
* **Notes** tab:
  * A Markdown document about the cell. It may be blank. It may be linked to any number of other Markdown files that are also in the cell co
* **Files** tab:
  * Ian arbitrary number of files and sub-folders
* **Chat** tab:
  * A chat stream shared with all members.

**Number of Members**

A cell can have just one member (the user) or several. We don’t currently know how big a cell can scale but the number is almost surely less (possibly a lot less) than 100.

**Write permissions**

Notes, files and chat are all read/write/editable by anyone in the cell. The permissions on who can write/edit which info fields vary.


 