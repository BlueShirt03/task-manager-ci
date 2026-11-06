variable "service_name" {
  description = "Name of the staging web service"
  type        = string
  default     = "task-manager-iac-staging"
}

variable "instance_plan" {
  description = "Render instance plan for staging"
  type        = string
  default     = "starter"

  validation {
    condition = contains(
      ["starter", "standard", "pro"],
      var.instance_plan
    )
    error_message = "Choose a supported Render instance plan."
  }
}

variable "region" {
  description = "Render region for the staging service"
  type        = string
  default     = "oregon"
}

variable "repo_url" {
  description = "GitHub repository URL for the FastAPI application"
  type        = string
}