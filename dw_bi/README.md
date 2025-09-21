# Giorno 2 – Data Warehouse + BI (Mini‑progetto)

Obiettivo: creare un piccolo **schema a stella** per un e‑commerce, caricarlo in **Postgres** e costruire una dashboard in **Metabase** (o Tableau Public).

## Struttura
```
data/                # CSV delle dimensioni e della fact
sql/                 # DDL, load e query analitiche
infra/               # docker-compose per Postgres + Metabase
```

## Avvio rapido (Docker)
1. Copia questa cartella in locale.
2. Crea un file `.env` (vedi sotto) accanto al docker-compose.
3. Avvia i servizi:
   ```bash
   docker compose -f infra/docker-compose.yml --env-file infra/.env up -d
   ```
4. Postgres sarà su `localhost:5433` (db: `dwdb`, user: `dwuser`). Metabase su `http://localhost:3000`.

### `.env` di esempio (infra/.env)
```env
POSTGRES_PASSWORD=dwpass
METABASE_ENCRYPTION_KEY=please_change_me_32_chars_min
```

### Caricamento dati
Entra nella shell psql del container:
```bash
docker exec -it dw-postgres psql -U dwuser -d dwdb
```
Dentro `psql` esegui:
```sql
\i /repo/sql/01_ddl.sql
\i /repo/sql/02_load.sql
\i /repo/sql/03_analytics.sql  -- per testare le query
```

> Nota: nel container i file del progetto sono montati in `/repo`.

## Dashboard in Metabase (quick steps)
1. Apri Metabase (http://localhost:3000) e completa l'onboarding.
2. Aggiungi database: Postgres → host `dw-postgres`, porta `5432`, db `dwdb`, user `dwuser`, password dal tuo `.env`.
3. Vai su **Browse data → dw → fact_orders** e usa **Summarize** per creare:
   - **Revenue by Category** (sum of `extended_amount` by `category`)
   - **Top Customers by Revenue** (sum of `extended_amount` by `customer_code`/`customer_name`)
   - **Monthly Revenue Trend** (sum of `extended_amount` grouped by `year` + `month` da `dim_dates`)
4. Salva ciascun grafico e aggiungilo ad una **Dashboard** chiamata “E‑commerce Overview”.
5. Fai uno **screenshot** della dashboard per l’output richiesto.

## BigQuery (alternativa)
- Crea un dataset `dw` su BigQuery free tier.
- Importa i CSV in tabelle `dim_customers`, `dim_products`, `dim_dates`, `fact_orders`.
- Adatta il DDL (rimuovi `schema dw.` e i tipi NUMERIC → BIGNUMERIC/FLOAT64 secondo necessità).
- Esegui le query di `03_analytics.sql` con sintassi BigQuery (JOIN identici).

## Consegna
- **Screenshot dashboard** (Metabase o Tableau Public)
- **Query SQL**: includi `03_analytics.sql` nel repo
- (Opzionale) Esporta Metabase dashboard .png e includila nel repo
```
