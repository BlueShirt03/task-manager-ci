terraform {
  required_version = ">= 1.5.0"

  required_providers {
    render = {
      source  = "render-oss/render"
      version = "~> 1.0"
    }
  }

  cloud {
    organization = "task-manager-iac"

    workspaces {
      name = "task-manager-iac-staging"
    }
  }
}