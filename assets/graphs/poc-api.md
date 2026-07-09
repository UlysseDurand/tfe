```mermaid
graph LR
    RadMenu
    RadItem -. Must be under .-> RadWheel
    RadialCheckbox --Extends--> RadItem
    RadWheel-. Must be under .-> RadMenu
    RadWheel -. Can be under .-> RadWheel
```