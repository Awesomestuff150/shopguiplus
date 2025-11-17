# Troubleshooting

## Database migration checklist
If you're migrating ShopGUIPlus data from SQLite to MySQL, double-check that you have recent backups, stop the server before copying files, and review each optional migration script before running it. If you run into issues, follow [Fix 1a – Optional MySQL migration](#fix-1a-optional-mysql-migration) for the supported MySQL workflow.

### Fix 1a – Optional MySQL migration
Use the optional MySQL migration script only if you understand the implications of changing storage engines. The following steps help prevent data loss:

1. Back up the `ShopGUIPlus` directory so you can roll back if anything goes wrong.
2. Configure your `config.yml` to point to the target MySQL server and verify the credentials work with another client first.
3. Run the migration script with the server stopped to avoid concurrent writes to the SQLite database.
4. After the script reports success, start the server and confirm the plugin loads data from MySQL.

If the script fails, inspect the console output for the exact SQL statement that errored, fix the data manually, and re-run the script. Always keep the original SQLite database until you're confident that the MySQL copy is working as expected.
