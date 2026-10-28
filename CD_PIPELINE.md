## Automated Staging Deployment Pipeline

# Overview and Tools 

The purpose of this project was to implement a Continuous Deployment (CD) pipeline that automatically deploys a FastAPI Task Manager appliactoin to a Staging environment after successfully passing Continuous Integration (CI) checks.

GitHub Actions was selected to automate the CI/CD process because the repository already used GitHub Actions for automated testing. Render was selected to host the Staging application because it supports Python applications and provides an API for triggering and monitoring deployments. Together, these tools allow the pipeline to test code changes, deploy validated Git commits, and verify that the application is running successfully.

# Deployment Process

The CI/CD pipeline is configured in .github/workflows/ci.yml and is triggered by pull requests and pushes to the main branch. The build-and-test job installs the required dependencies, runs automated tests using Pytest, and validates Python compilation. If these checks pass, the application files are packaged into a ZIP artifact and uploaded to GitHub Actions.

After the changes are merged into main, the deploying-staging job runs. This job downloads and validates the build artifact before using the Render API to deploy the same Git commit that passed CI testing. The deployment job only runs after build-and-test succeeds, preventing failed builds from being automatically deployed to Staging.

# Staging Configuration

A separate staging environment was created in GitHub Actions and configured to allow deployments from the main branch. The Render web service was configured with APP_ENV=staging, while the application uses development as its default environment when the variable is not set.

Sensitive credentials, including RENDER_API_KEY and RENDER_DEPLOY_HOOK_URL, were stored as GitHub environment secrets rather than directly in the workflow file. The RENDER_SERVICE_ID and STAGING_URL were configured as environment variables. Render's automatic deployment option was disabled so that GitHub Actions controls when deployments occur.



# Verification and Results

After triggering the deployment, the pipeline uses the Render API to monitor its status and verify that the deployed Git commit matches the commit tested by CI. If the deployment fails or the commits do not match, the workflow stops and reports an error.

Once the deployment is successful, an automated smoke test sends an HTTP GET request to the Staging application's root endpoint. The test checks for an HTTP 200 status code and verifies that the application returns the expected JSON response. If the test fails, the pipeline retries before reporting an error.

The final GitHub Actions workflow completed successfully, with both build-and-test and deploying-staging passing. Render confirmed that the application was live, and the automated smoke test passed.

Live Staging URL: https://task-manager-staging-nfoq.onrender.com