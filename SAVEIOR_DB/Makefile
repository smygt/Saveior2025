.PHONY: up down load-demo clean

# Start the database container
up:
	docker-compose up -d

# Stop and remove the database container
down:
	docker-compose down

# Load demo data into the database
load-demo:
	docker exec -i saveior2025-db-1 psql -U postgres -d saveior < ./demo_data.sql

# Remove demo data from the database
remove-demo:
	docker exec -i saveior2025-db-1 psql -U postgres -d saveior -c "DELETE FROM link_tags; DELETE FROM link_folders; DELETE FROM links; DELETE FROM tags; DELETE FROM folders;"

# Clean up all containers and volumes
clean:
	docker-compose down -v

# Initialize database with schema and demo data
init: up load-demo

# Reset database (remove everything and start fresh)
reset: clean init

# Show database logs
logs:
	docker-compose logs -f 