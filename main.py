import tkinter as tk
from tkinter import font as tkfont
import re

from ingredient_bank import IngredientBank


class UI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title_font = tkfont.Font(family="Helvetica", size=18)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="true")

        self


def remove_brackets(string):
    return re.sub(r"(\s\(((?!\().)*\))", '', string)


def prep_list(string):
    string = remove_brackets(string)
    string = string.lower()
    return string.split(", ")


if __name__ == '__main__':
    # ui = UI()
    # ui.mainloop()

    account = IngredientBank("Lana")
    bha = "Water (Aqua), Methylpropanediol (hydration), Butylene Glycol (hydration), Salicylic Acid (beta hydroxy acid/exfoliant), Polysorbate 20 (stabilizer), Camellia Oleifera Leaf Extract (green tea/skin calming/antioxidant), Sodium Hydroxide (pH balancer), Tetrasodium EDTA (stabilizer)"
    madagascar = "Centella Asiatica Extract ( 72 % ), Glycerin, Propanediol, Dipropylene Glycol, Cyclomethicone, Water, 1, 2 - Hexanediol, Trehalose, Caprylyl Methicone, C12 - 14 Pareth - 12, Carbomer, Tromethamine, Ammonium Acryloyldimethyltaurate / VP Copolymer, C30 - 45 Alkyl Cetearyl Dimethicone Crosspolymer, Xanthan Gum, Mentha P. Piperita ( Peppermint ) Leaf Extract, Zingiber Officinale ( Ginger ) Root Extract, Butylene Glycol, Ethylhexylglycerin, Dipotassium Glycyrrhizate, Tranexamic Acid, Coptis Chinensis Root Extract, Theobroma Cacao ( Cocoa ) Extract, Dextrin, Leuconostoc / Radish Root Ferment Filtrate, Biosaccharide Gum - 1. Disodium EDTA, Sodium Hyaluronate, Beta-Glucan, Ceramide EOP. Ceramide NS, Ceramide NP, Ceramide AP, Phytosphingosine, Hydrogenated Lecithin, Cetearyl Alcohol, Stearic Acid, Cholesterol"
    centella = "Centella Asiatica Leaf Water, Melaleuca Alternifolia (Tea Tree) Leaf Water, Butylene Glycol, Water, Niacinamide, Methyl Trimethicone, Acrylates/C10-30 Alkyl Acrylate Crosspolymer, Arginine, 1,2-Hexanediol, Caprylyl Glycol, Dimethicone, Dimethicone/Vinyl Dimethicone Crosspolymer, Centella Asiatica Extract, Allantoin, Melaleuca Alternifolia (Tea Tree) Leaf Extract, Ethylhexylglycerin, Adenosine, Dipotassium Glycyrrhizate, Citrus Aurantium Bergamia (Bergamot) Fruit Oil, Pentylene Glycol, Sodium Hyaluronate, Aspalathus Linearis Extract, Glycyrrhiza Glabra (Licorice) Root Extract, Triticum Vulgare (Wheat) Germ Extract, Brassica Oleracea Italica (Broccoli) Extract, Brassica Oleracea Capitata (Cabbage) Leaf Extract, Medicago Sativa (Alfalfa) Extract, Raphanus Sativus (Radish) Seed Extract, Brassica Campestris (Rapeseed) Extract, Yucca Schidigera Root Extract, Commiphora Myrrha Resin Extract, Perilla Frutescens Leaf Extract, Limonene, Linalool"
    honest = "Water (Aqua), Squalane, Glycerin, Polyglyceryl-4 lsostearate, Pyrus Malus (Apple) Fruit Extract, Coco-Caprylate/Caprate, Propanediol, Disteardimonium Hectorite, Jojoba Esters, Sodium PCA, Tocopherol, Sodium Acetylated Hyaluronate, Hydrolyzed Sodium Hyaluronate, Trisodium Ethylenediamine Disuccinate, 1,2-Hexanediol, Caprylhydroxamic Acid."
    versed = "Water, Helianthus Annuus (Sunflower) Seed Oil, Sodium Acrylate/Sodium Acryloyldimethyl Taurate Copolymer, Retinol, Bakuchiol, Crithmum Maritimum Extract, Glycerin, Paeonia Suffruticosa Extract, Butyrospermum Parkii (Shea) Butter, Hydroxypropyl Cyclodextrin, Sodium Hyaluronate, Carica Papaya Extract, Xylitylglucoside, Anhydroxylitol, Xylitol, Hippophae Rhamnoides Oil, Tocopheryl Acetate, Opuntia Conccinellifera Fruit Extract, Rosa Canina Seed Oil, Chamomilla Recutita (Matricaria) Extract, Aloe Barbadensis Leaf Juice, Chlorophyll, Caprylic/Capric Triglyceride, Hydrogenated Vegetable Oil, Nylon-12, Isohexadecane, Polysorbate 80, Trehalose, Leuconostoc/Radish Root Ferment Filtrate, Phenoxyethanol, Ethylhexylglycerin"
    elf = "WATER (AQUA), ISOHEXADECANE, STEARYL HEPTANOATE, GLYCERIN, BUTYLENE GLYCOL, ISOPROPYL ISOSTEARATE, NIACINAMIDE, CETEARYL OLIVATE, TREHALOSE, SQUALANE, DIMETHICONE, STEARIC ACID, ALUMINUM STARCH OCTENYLSUCCINATE, POLYMETHYLSILSESQUIOXANE, SILICA, SODIUM HYALURONATE, PALMITOYL TRIPEPTIDE-1, PALMITOYL TETRAPEPTIDE-7, PANTHENOL, SORBITAN OLIVATE, CETEARYL ALCOHOL, GLYCERYL STEARATE, PEG-100 STEARATE, POLYETHYLENE, DISODIUM EDTA, POLYACRYLATE-13, POLYISOBUTENE, POLYSORBATE 20, CAPRYLYL GLYCOL, PHENOXYETHANOL, ETHYLHEXYLGLYCERIN, CARBOMER"
    cerave = "Aqua, Glycerin, Caprylic/Capric Triglycerides, Niacinamide, Behentrimonium Methosulfate and Cetearyl Alcohol, Ceteareth-20 and Cetearyl Alcohol, Dimethicone, Ceramide NP, Ceramide AP, Ceramide EOP, Phytosphingosine, Cholesterol, Hyaluronic Acid, Sodium Lauroyl Lactylate, Polyglyceryl-3 Diisostearate, Disodium EDTA, Potassium Phosphate, Dipotassium Phosphate, Methylparaben, Propylparaben, Carbomer, Xanthan Gum"
    paula_niac = "Water (Aqua), Niacinamide (vitamin B3, skin-restoring ), Acetyl Glucosamine (skin replenishing/antioxidant), Ascorbyl Glucoside (vitamin C/antioxidant), Butylene Glycol (hydration), Phospholipids (skin replenishing), Sodium Hyaluronate (hydration/skin replenishing), Allantoin (skin-soothing), Boerhavia Diffusa Root Extract (skin-soothing), Glycerin (hydration/skin replenishing), Dipotassium Glycyrrhizate (skin-soothing), Glycyrrhiza Glabra Root Extract (licorice extract/skin-soothing), Ubiquinone (antioxidant), Epigallocatechin Gallate (antioxidant), Beta-Glucan (skin-soothing/antioxidant), Panthenol (skin replenishing), Carnosine (antioxidant), Genistein (antioxidant), Citric Acid (pH balancing), Sodium Citrate (pH balancing), Sodium Hydroxide (pH balancing), Xanthan Gum (texture-enhancing), Disodium EDTA (stabilizer), Ethylhexylglycerin (preservative), Phenoxyethanol (preservative)."
    spf_gel = "Water, ethanol, ethylhexyl methoxycinnamate, ethylhexyl triazone, isopropyl palmitate, (lauryl methacrylate / Na methacrylate) crosspolymer, diethylaminohydroxybenzoylhexylbenzoate, hydrogenated polyisobutene, bisethylhexyl oxyphenol methoxyphenyl triazine, palmitic acid Dextrin, BG, xylitol, (acrylate / alkyl acrylate (C10-30)) crosspolymer, dimethicone, alkyl benzoate (C12-15), glycerin, glyceryl stearate, propanediol, glyceryl behenate, (vinyl dimethicone / methicone Silsesquioxane) crosspolymer, cetanol, agar, sorbitan distearate, isoceteth-20, polyvinyl alcohol, (dimethicone / vinyl dimethicone) Suporima, stearoyl glutamate, arginine, hydroxide K, hydroxide Na, royal jelly extract, hyaluronic acid Na, phenoxyethanol, EDTA-2Na, BHT, perfume"
    spf_ess = "Ethylhexyl methoxycinnamate, cross-polymer of (lauryl methacrylate / sodium methacrylate), alkyl benzoate (C12-15), bisethylhexyloxyphenol methoxyphenyl triazine, hexyl diethylaminohydroxybenzoylbenzoate, dimethicone, ethylhexyl triazone , Dimethylsilylated silica, DPG, xylitol, dextrin palmitate, (acrylates / alkyl (C10-30)) crosspolymer, (dimethicone / vinyldimethicone) crosspolymer, polysilicone-9, glyceryl stearate, AMP, Vinyl dimethicone / methicone silsesquioxane) crosspolymer, agar, isoceteth-20, alkyl (C30-45) methicone, polyvinyl alcohol, olefin (C30-45), sodium hydroxide BG, PG, hyaluronic acid Na, royal jelly, orange fruit extract, grapefruit fruit extract, lemon fruit extract, phenoxyethanol, EDTA-2Na, BHT, perfume"
    # word parser (add such that water|aqua is an item)

    account.add_product(prep_list(bha), compatible=True)
    account.add_product(prep_list(madagascar), compatible=True)
    account.add_product(prep_list(centella), compatible=True)
    account.add_product(prep_list(honest), compatible=False)
    account.add_product(prep_list(paula_niac), compatible=False)
    account.add_product(prep_list(spf_gel), compatible=True)
    account.check_product(prep_list(versed))
    account.check_product(prep_list(elf))
    account.check_product(prep_list(cerave))
    account.check_product(prep_list(spf_ess))
    # account.close()
