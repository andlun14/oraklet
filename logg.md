Tärningsfel:
1. Inom funktionen för datorns tur så använde jag koden: random.randint(dator_bank / 10, dator_bank / 2) men det blev en error när det var andra rundan och datorns tur.
2. Felet var på grund av att dator_bank/10 och dator_bank/2 inte blir integers efter första rundan då om dator_bank är till exempel 550 så ska koden slumpa mellan 55 och 22.5 som alltså betyder att båda talen inte är integers.
3. Jag löste det genom att lägga till int() runt de två talen så att de blev omvandlade till integers innan random.randint försökte slumpa mellan dem.
4. Jag borde ha tänkt på att det skulle blir ett problem redan i början när jag skrev koden och gjort det så att talen garanterat är int's.