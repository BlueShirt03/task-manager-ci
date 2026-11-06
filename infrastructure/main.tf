resource "render_web_service" "staging" {
  name   = var.service_name
  plan   = var.instance_plan
  region = var.region

  runtime_source = {
    native_runtime = {
      runtime             = "python"
      repo_url            = var.repo_url
      branch              = "main"
      build_command       = "pip install -r requirements.txt"
      auto_deploy_trigger = "off"
    }
  }
  start_command     = "uvicorn app:app --host 0.0.0.0 --port $PORT"
  health_check_path = "/"
}