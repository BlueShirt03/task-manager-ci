output "staging_service_id" {
  description = "ID of the Terraform-managed staging service"
  value       = render_web_service.staging.id
}

output "staging_service_url" {
  description = "Public URL of the staging application"
  value       = render_web_service.staging.url
}

output "staging_service_name" {
  description = "Name of the staging web service"
  value       = render_web_service.staging.name
}