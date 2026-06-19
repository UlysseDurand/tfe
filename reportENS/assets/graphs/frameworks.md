```mermaid
graph TD
    Paraview:::nocode --> VTK:::cpp 
    Slicer[3D Slicer]:::nocode --> VTK
    SlicerWrap[3D Slicer wrapping]:::python --> Slicer
    VTKJs[VTK.js]:::js
    Vue[VueJS]:::js
    trame[trame]:::python --> Vue
    trame-vtk[trame-vtk]:::python --> VTKJs
    trame-vtk --> VTK
    trame-vtk --> trame
    trame-slicer:::python --> SlicerWrap
    trame-slicer --> trame
    trame-rca:::python --> trame
    trame-slicer --> trame-rca
    Vuetify:::js --> Vue
    trame-vuetify:::python --> Vuetify
    trame-vuetify --> trame
    trame-slicer --> trame-vuetify

    classDef python fill:#ff8080
    classDef js fill:#4dabf7
    classDef cpp fill:#60d060
    classDef nocode fill:#ffaaff
    ```