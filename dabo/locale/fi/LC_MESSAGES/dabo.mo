��          �      ,      �     �  C   �  z   �  �   O      /  *   P  +   {     �     �  .   �  ?   �  �  "  /   �     �  "   �  "     �  9     �  J   �  �   %  �   �  /   �	  <   �	  >   %
     d
     g
  ;   p
  O   �
  �  �
  5   �     �  (   �  1                                      
                                       	    Cancel Could not access the database with the given username and password. DBA, please enter the username and password that has access to create tables for database on server '%s' and database '%s' For the DB Admin:
 The tables must either created by:
  1. using this program by TEMPORARLY giving this program access to the database to create the needed tables.
  2. or executing all the quries in the 'queries.sql' file. No key field defined for table:  No table has been defined for this bizobj. No tables have been setup for autocreation. OK Password Text to display for null (None) values.  (str) The database could not be setup. Contact your DB administrator. The object reference to the main form of the application, or None.

			The MainForm gets instantiated automatically during application setup, 
			based on the value of MainFormClass. If you want to swap in your own
			MainForm instance, do it after setup() but before start(), as in:

			>>> import dabo
			>>> app = dabo.dApp()
			>>> app.setup()
			>>> app.MainForm = myMainFormInstance
			>>> app.start() The table definition for this bizobj.  (object) Username You must enter the password first. You must enter the username first. Project-Id-Version: dabo
Report-Msgid-Bugs-To: FULL NAME <EMAIL@ADDRESS>
POT-Creation-Date: 2007-08-26 10:04+0000
PO-Revision-Date: 2007-07-31 20:27+0000
Last-Translator: Lauri Ojansivu <Unknown>
Language-Team: Finnish <fi@li.org>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Launchpad-Export-Date: 2008-11-29 16:28+0000
X-Generator: Launchpad (build Unknown)
 Hylkää Ei saatu yhteyttä tietokantaan annetulla käyttänimellä ja salasanalla. Tietokannan ylläpitäjä, ole hyvä ja kirjoita käyttäjänimi ja salasana joilla on oikeudet luoda taulukot palvelimelle '%s' ja tietokantaan '%s' Tietokannan ylläpitäjälle:
 Taulukot täytyy luoda joko:
  1. käytämällä tätä ohjelmaa antaen VÄLIAIKAISESTI tälle ohjelmalle oikeudet tehdä tarvittavat taulukot tietokantaan.
  2. tai suorittamalla kaikki kyselyt 'queries.sql' tiedostosta. Avainkenttää ei ole määritelty taulukolle:  Yhtään taulukkoa ei ole määritelly tälle Bizobjektille. Yhtään taulukkoa ei ole asetettu luotavaksi automaattisesti. OK Salasana Teksti joka näytetään null (Ei mitään) arvoille. (str) Tietokantaa ei pystytty asettamaan. Ota yhteyttä tietokannan ylläpitäjään. Objektin viittaus ohjelman päälomakkeeseen, tai Ei mitään.

			Päälomakkeesta luodaan esiintymä automaattisesti ohjelmaa asetettaessa,
			perustuen arvoon MainFormClass:issa. Jos haluat vaihtaa siihen oman
			MainForm esiintymäsi, tee se setup():n jälkeen mutta ennen start():ia, kuten seuraavassa:

			>>> import dabo
			>>> app = dabo.dApp()
			>>> app.setup()
			>>> app.MainForm = myMainFormInstance
			>>> app.start() Taulukon määritelmä tälle Bizobjektille. (object) Käyttäjätunnus Sinun täytyy kirjoittaa salasana ensin. Sinun täytyy kirjoittaa käyttäjätunnus ensin. 