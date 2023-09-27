### NO TES!

#### TODO: 
- [X?] finnish check_actions
    - [ ] make shit and run in-file
- [ ] run unit tests
- [ ] make and run integration test
- [ ] test the different algos
- [ ] collectin into notebook
  - [X] copy the structure from the original file
  - [ ] paste inn all the functions

frista ganske å hiv shit inn i mappa for å clean dir, men idno, fakka jo me alle imports

ang oppgaven, burde vi se på både om di forskjellie search algoan kan løs forksjelli wh, men også kor mange steps? og kor lang tid d tar å compute shit?

blir table me forskjelli algo, forskjelli huerisitc. \
nvm trur vi treng et table for hver


## Uniform Cost Search
| Warehouse Id | Solved | Steps Used | Time Taken |
|----------------|--------|------------|------------|
|  1    | Yes    | 50         | 10.5s      |
|  2    | Yes    | 40         | 8.2s       |
|  3    | No     | -          | -          |
| ...            | ...    | ...        | ...        |


## Greedy Search
| Warehouse Id | Solved | Steps Used | Time Taken |
|----------------|--------|------------|------------|
|  1    | Yes    | 50         | 10.5s      |
|  2    | Yes    | 40         | 8.2s       |
|  3    | No     | -          | -          |
| ...            | ...    | ...        | ...        |


om vi lagra dataene kan vi gjør enkle anallysa på d:
- antall solved
- avg time
- avg steps
- bargraph for :
  - kordan wh va vanskeli
  - kordan forskjellli algo presterte på enkelte wh
  - se mock_analysis.png