# Docker Build Fix for Frontend Service

## Issue Description
The frontend service Docker build was failing with the error:
```
failed to solve: process "/bin/sh -c npm ci --only=production" did not complete successfully: exit code: 1
```

## Root Causes Identified

### 1. Missing package-lock.json
The `npm ci` command requires a `package-lock.json` file to work properly, but this file was missing from the frontend directory.

### 2. Wrong npm flags for React build
The Dockerfile was using `npm ci --only=production`, which only installs production dependencies. However, React builds require development dependencies like `react-scripts` to execute the `npm run build` command.

## Solution Applied

### Changed Dockerfile command
**Before:**
```dockerfile
RUN npm ci --only=production
```

**After:**
```dockerfile
RUN npm install
```

### Why this fixes the issue:
1. `npm install` works without requiring a `package-lock.json` file
2. `npm install` installs both production and development dependencies, which are needed for the React build process
3. Since this is a multi-stage build, the final image will only contain the built static files served by nginx, so the development dependencies don't affect the final image size

## Alternative Solutions (for future consideration)

### Option 1: Generate package-lock.json
If you prefer to use `npm ci` for reproducible builds:
1. Run `npm install` locally to generate `package-lock.json`
2. Commit the `package-lock.json` file
3. Change the Dockerfile to use `npm ci` (without `--only=production`)

### Option 2: Use separate install commands
```dockerfile
RUN npm ci
# This installs all dependencies, then builds
RUN npm run build
```

## Testing the Fix
To test the fix, run:
```bash
docker-compose build frontend
```

The build should now complete successfully.