This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## General Notes - pypokelib:

* Pokemon library that allows users to create “fully fleshed out” Pokemon instances  with a simple call.
    - Pokemon(“charmander”) creates a charmander instance with all corresponding attributes (hp, atk, nature, dex#, etc.)
    - Pokemon(4) also does the same as above
    - Wanted to have flexibility between creating instance by name vs by dex#, without having to say something like Pokemon(species=“Charmander”) or Pokemon(dex_num=4), bc that’s annoying and kinda ugly
* Library split by generation, as different generations have different stats, functionality, inherent compatibility issues, etc.
    - Individual Pokemon information hard-coded in lookup tables, for fast access time, and not having to rely on external API such as PokeAPI
    - Fast lookup times and simple, intuitive calling conventions make this a great library to use with pygame, to build custom Pokemon clone, e.g.
    - Easy to alter instance variables as necessary, either with built-in functions or directly
    - Technically, since there are no enforced private variables in Python, someone could potentially mess up the _base_stats, data member, _types, _tmhm_learnset, etc., but because they are prefixed by underscore, it is implied by convention that one should not attempt to access these outside of class definition. Preferred this over name mangling (dunder variable) bc even that isn’t truly private. Just be responsible
    - Future update: include sprites (and shiny)!
