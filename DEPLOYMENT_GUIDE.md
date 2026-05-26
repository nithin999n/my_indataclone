# Deployment Guide for Render

## Changes Made:
✅ Changed database from MySQL to SQLite3
✅ Removed mysqlclient dependency
✅ Updated settings.py for production
✅ Added WhiteNoise for static files
✅ Created requirements.txt
✅ Created build.sh for Render
✅ Added .gitignore
✅ All code committed to git

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `my_indataclone`
3. Description: "InDataAI Clone - Django Web Application"
4. Choose Public or Private
5. **DO NOT** check "Initialize with README"
6. Click "Create repository"

## Step 2: Push Code to GitHub

After creating the repository, run:

```bash
cd e:\my_indataclone
git push -u origin main
```

If you need authentication:
- Use your GitHub username
- For password, use a Personal Access Token (not your GitHub password)
- To create token: GitHub Settings → Developer settings → Personal access tokens → Generate new token
- Select scope: `repo` (full control)

## Step 3: Deploy on Render

1. Go to https://render.com and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub account
4. Select the `my_indataclone` repository
5. Configure the service:

### Basic Settings:
- **Name**: `indataai-clone` (or your preferred name)
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: (leave empty)
- **Runtime**: `Python 3`

### Build & Deploy:
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn indata_project.indata_project.wsgi:application`

### Environment Variables (click "Add Environment Variable"):
1. **SECRET_KEY**: 
   - Generate a new one: https://djecrety.ir/
   - Example: `django-insecure-xyz123abc456...`

2. **DEBUG**: `False`

3. **ALLOWED_HOSTS**: 
   - Will be: `your-app-name.onrender.com`
   - Example: `indataai-clone.onrender.com`

4. **PYTHON_VERSION**: `3.11.0` (optional, Render auto-detects)

### Advanced Settings:
- **Auto-Deploy**: Yes (recommended)
- **Instance Type**: Free (or paid if you prefer)

6. Click "Create Web Service"

## Step 4: Wait for Deployment

- Render will automatically:
  1. Clone your repository
  2. Install dependencies from requirements.txt
  3. Run build.sh (collectstatic and migrate)
  4. Start the application with gunicorn

- First deployment takes 5-10 minutes
- Watch the logs for any errors

## Step 5: Access Your Application

Once deployed, your app will be available at:
`https://your-app-name.onrender.com`

## Important Notes:

### SQLite on Render:
- ⚠️ SQLite data is **ephemeral** on Render free tier
- Database resets when service restarts
- For production, consider upgrading to PostgreSQL

### Static Files:
- WhiteNoise serves static files automatically
- No need for separate CDN on free tier

### Admin Panel:
- Access at: `https://your-app-name.onrender.com/admin/`
- Create superuser after deployment:
  1. Go to Render Dashboard → Your Service → Shell
  2. Run: `python indata_project/manage.py createsuperuser`
  3. Follow prompts

### Contact Form:
- Contact form submissions save to SQLite database
- Access via admin panel

## Troubleshooting:

### If deployment fails:
1. Check Render logs for errors
2. Verify all environment variables are set
3. Ensure build.sh has execute permissions

### If static files don't load:
1. Check ALLOWED_HOSTS includes your Render URL
2. Verify STATIC_ROOT is set correctly
3. Run collectstatic manually in Render shell

### If you get "Bad Request (400)":
- Add your Render URL to ALLOWED_HOSTS environment variable

## Upgrading to PostgreSQL (Recommended for Production):

1. In Render Dashboard, create a new PostgreSQL database
2. Copy the Internal Database URL
3. Update requirements.txt:
   ```
   Django==5.2.13
   gunicorn==21.2.0
   whitenoise==6.6.0
   django-cors-headers==4.3.1
   psycopg2-binary==2.9.9
   dj-database-url==2.1.0
   ```
4. Update settings.py DATABASES to use DATABASE_URL
5. Add DATABASE_URL to environment variables
6. Redeploy

## Support:

- Render Docs: https://render.com/docs
- Django Docs: https://docs.djangoproject.com/
- Your GitHub Repo: https://github.com/nithin999nth/my_indataclone

Good luck with your deployment! 🚀
