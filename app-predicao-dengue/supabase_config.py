from supabase import create_client, Client

SUPABASE_URL = "https://vhjpowbnygpocqrdrucp.supabase.co"
SUPABASE_KEY = 'process.env.SUPABASE_KEY'
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
