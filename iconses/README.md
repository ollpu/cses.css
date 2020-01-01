## Iconses workflow

- Revise/design the icon in FreeCAD. There are parameters in the `ss` spreadsheet!
- Export an SVG from FreeCAD. I exported all the icons at once, which is messy
  but works for now.
- Clean them up with Inkscape
  - Press `Ctrl-U` with an icon selected to "ungroup" it, thus cleaning out any
    wierd transforms FreeCAD left there.
  - Make separate SVGs for each icon and name them appropriately.
- Convert to an icon font with `icon-font-generator` from npm.
```
icon-font-generator set/*.svg -o [target] -n Iconses
```
  - This is quite brittle now, since the icons will be given codepoints solely
    based on their alphabetical order. This will need to be done diffently in
    the future (maybe use the underlying library that icon-font-generator uses?)
