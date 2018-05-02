As the brief description indicates, this is built to produce three Annotation Scripts for three of the large tables used in the game No Man's Sky. These are the Technology, Product, and Substance Tables. Currently these ***do not*** annotate the substances/products used to charge and/or craft equipment/tech/products, as I had trouble figuring out a way to write this to do so.

Nevertheless, it *does* annotate the names of every Technology, Product, and Substance in these tables, which should prove helpful in translating the charging/crafting requirements.

At the moment, I'm currently considering adding a fourth script to be generated for the Alien Puzzle Table, but I decided this was a solid start. Hope you may find this useful!

P.S. Remember to open each generated script and set ET.Parse to target the correct files (however you have them named, if differing from the vanilla, decompiled names). 

Also, the Product script will require you to escape the apostrophes for a few products for it to work properly. The specific products are noted in a comment at the top of the script, so please make sure to keep this in mind before running it!

**NEW!**  
The MissionTable Annotation Script Generator is essentially the same as the Tech/Product/SubstanceTable Annotation Script Generator, with the caveat that it *will not* produce separate scripts for each MissionTable with a single run. Due to the convoluted structure of the Mission Tables, I've simply left it so that you must revise the ET.Parse target for the table you want to produce an annotating script for. 

While this is less convenient, it is nevertheless better than nothing, and I hope will help those interested in navigating the Mission Tables. That said, this uses a different method to the above generator to annotate the various lines, so one needn't worry about escaping apostrophes in the produced script, so hopefully that makes up a bit for the inconvenience of having to readjust the generator for each table.
