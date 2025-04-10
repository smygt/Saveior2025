FROM postgres:15

# Set environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=saveior

# Create initialization directory
RUN mkdir -p /docker-entrypoint-initdb.d

# Copy initialization scripts
COPY schema.sql /docker-entrypoint-initdb.d/01-schema.sql

# Make sure the script is executable
RUN chmod 755 /docker-entrypoint-initdb.d/01-schema.sql



# Expose the PostgreSQL port
EXPOSE 5432

# Set the working directory
WORKDIR /docker-entrypoint-initdb.d

# Command to run PostgreSQL
CMD ["postgres"] 