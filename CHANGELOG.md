# Changelog for pypokelib
# All dates in YYYY-MM-DD format

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).




## [Unreleaed] ========================================================================================================
- Support for unique learnsets of all Pokemon




## [0.1.1] - 2023-08-04 ===============================================================================================

## Fixed
- Hellish imports à la Java. No more "from pypokelib.generation1.data.pokemon.basestats.poke_base_class import Pokemon"

## Added
- Not really *added* but started work on moves and movesets. Much more to come

## [0.1.0] - 2023-08-03 ===============================================================================================

### Added
- Fully functional core feature, Pokemon() constructor, callable outside of class module (main.py)
- Installed a "lines of code" counter, which put a .DS_Store file everywhere... Positive side effect:
- Now the entire library structure (empty directories too) is visible on GitHub

## Changed
- Old code was moved to... _OLD_CODE directory... how original

## [0.1.0-beta.3] - 2023-08-03 =======================================================================================

### Added
- Preliminary performance tests (yes, yes, premature optimization == bad, just wanted to take a spin around the block)

## Removed
- Unnecessary helper table (converted int->str to search by str and return str anyway??? huh???)

## [0.1.0-beta.2] - 2023-08-03 =======================================================================================

### Added
- Inits to each directory, effectively making each directory a Python package
- POKEDEX dictionary, allowing for fast lookup times
- Calling Pokemon("Squirtle") and Pokemon(7) now works as intended! Though only in file containing Pokemon base class

## Changed
- Pokemon base class constructor, more robust (methods, data members), uses fast lookup operations
- Renamed certain files, see GitHub repo for more details

## [0.1.0-beta.1] - 2023-08-02 =======================================================================================

### Added
- Committed to the idea of a single base Pokemon class: much simpler and easier to maintain
- Defined some basic class methods, more to come

## Changed
- Allowed the base Pokemon class constructor to accept either a string containing the species name, or the pokedex id
- That is, Pokemon("Squirtle") and Pokemon(7) should mean the same thing

## Removed
- Abra class, and the idea of having a separate class for each all 151 Pokemon

## [0.1.0-alpha.2] - 2023-08-01 =======================================================================================

### Added
- This version has initial insights of how I want(ed) to call certain methods when completed with pypokelib
- At this point, I was still considering having a class for each of 151 pokemon, but...
- Began work on a Pokemon base class, rather than making a dedicated class for all 151

## [0.1.0-alpha.1] - 2023-08-01 =======================================================================================

### Added
- Created initial repository, threw around initial ideas for library structure
- Wrote functions for calculating stats based on level, nature
- Brainstormed ideas for how to instanstiate pokemon objects, and what data to track
- Fiddled around with datasets

## - Links to previous versions =======================================================================================

[unreleased]: https://github.com/whatever-path-idk-right-now/HEAD

[1.1.1]:
[1.1.0]:
[1.0.0]:
[0.3.0]:
[0.2.0]:
[0.1.0]:
[0.0.8]:
[0.1.1]: 
[0.1.0]: https://github.com/julius-alexander/pypokelib/commit/13c5d2fa1993c5bf8dcd28ae5e50d18a1c358a21
[0.1.0-beta.3]: https://github.com/julius-alexander/pypokelib/commit/2bc3c7e278cbf3814ffd0f65bc45b48fd5eb2558
[0.1.0-beta.2]: https://github.com/julius-alexander/pypokelib/commit/d8c3a695f20d6451c597ce425dceda78f730f233
[0.1.0-beta.1]: https://github.com/julius-alexander/pypokelib/commit/2c52c5b42fa8fb3c7250b22f31e933ef0bcfa4de
[0.1.0-alpha.2]: https://github.com/julius-alexander/pypokelib/commit/e6e94d364f0ab6aca5539f5aba82fbd64236d641
[0.1.0-alpha.1]: https://github.com/julius-alexander/pypokelib/commit/62d85802fa4d6c0085ff2ccdd64e0c16689b99ce#diff-a82f26b5140e08a460701432765894bf8f80009cdeea5e3a96e2398f16a34059
