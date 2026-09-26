"""Exploration du fichier Sirene StockUniteLegale (lecture seule)."""

import pyarrow.parquet as pq

# Chemin du fichier téléchargé
CHEMIN = "data/raw/sirene/StockUniteLegale.parquet"

# Ouvre le fichier sans charger les données en mémoire
fichier = pq.ParquetFile(CHEMIN)

# Nombre total de lignes, lu dans les métadonnées
print("Lignes :", fichier.metadata.num_rows)

# Liste des colonnes et de leur type
print("\n=== SCHÉMA ===")
print(fichier.schema_arrow)

# Aperçu des 5 premières lignes, transposé pour la lisibilité
print("\n=== APERÇU ===")
print(next(fichier.iter_batches(batch_size=5)).to_pandas().T)
