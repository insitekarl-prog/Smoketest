# Standalone HTML refresh smoke test

`data.json` → Python generator → self-contained `site/index.html` → GitHub Actions → Azure Static Web Apps.

## Local preview

From the repository root, run `python3 smoke-test/scripts/build.py`, then open `smoke-test/site/index.html`.
The HTML contains all its content and styling; it needs no runtime API or libraries.

## Connect deployment

1. Push this repository to the intended GitHub repository, using `main`.
2. Create or select an Azure Static Web App. Use its deployment token to set the GitHub repository Actions secret named `AZURE_STATIC_WEB_APPS_API_TOKEN`. Enter the token directly in GitHub; do not put it in a file or chat.
3. Use the workflow supplied here; avoid enabling a second generated deployment workflow for the same app.
4. Run **HTML data refresh smoke test** from GitHub Actions and open the Azure URL.

## Prove refresh works

1. Confirm the deployed page shows “First smoke test”, value `1`, a UTC generation timestamp, and the deployed commit SHA.
2. Change `data.json` to a new message and value `2`, commit, and push to `main`.
3. Wait for the deployment workflow to succeed.
4. Confirm the SAME Azure URL displays the new message, value `2`, and new SHA. An already-open page reloads every 60 seconds; hosting configuration disables caching.

A successful local build does not prove cloud deployment. The smoke test passes only after both deployed versions are checked.

## Real data

The starter reads sample data committed to GitHub. It does not yet fetch an external source or schedule refreshes. Once a source and cadence are selected, the workflow can fetch fresh data before generation and run on a schedule. Browser reloads alone do not update source data.

Deployment references:
- https://learn.microsoft.com/en-us/azure/static-web-apps/build-configuration
- https://docs.github.com/en/actions/how-tos/deploy/deploy-to-third-party-platforms/azure-static-web-app
