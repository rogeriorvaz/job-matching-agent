PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS cv_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    version TEXT,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    source_job_id TEXT,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT,
    salary_text TEXT,
    salary_min INTEGER,
    salary_max INTEGER,
    description TEXT,
    url TEXT NOT NULL,
    canonical_url TEXT,
    posted_at TEXT,
    discovered_at TEXT NOT NULL,
    updated_at TEXT,
    job_hash TEXT UNIQUE,
    status TEXT DEFAULT 'new'
);

CREATE TABLE IF NOT EXISTS job_sources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    source TEXT NOT NULL,
    source_job_id TEXT,
    url TEXT,
    discovered_at TEXT NOT NULL,
    FOREIGN KEY (job_id) REFERENCES jobs(id)
);

CREATE TABLE IF NOT EXISTS job_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    cv_profile_id INTEGER,
    role_alignment REAL NOT NULL,
    responsibility_alignment REAL NOT NULL,
    technical_skills REAL NOT NULL,
    delivery_agile REAL NOT NULL,
    leadership_seniority REAL NOT NULL,
    domain_relevance REAL NOT NULL,
    location_fit REAL NOT NULL,
    raw_score REAL NOT NULL,
    penalty REAL NOT NULL DEFAULT 0,
    final_score REAL NOT NULL,
    confidence REAL,
    recommendation TEXT,
    strengths TEXT,
    gaps TEXT,
    missing_requirements TEXT,
    model TEXT,
    scored_at TEXT NOT NULL,
    FOREIGN KEY (job_id) REFERENCES jobs(id),
    FOREIGN KEY (cv_profile_id) REFERENCES cv_profiles(id)
);

CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL UNIQUE,
    status TEXT DEFAULT 'saved',
    applied_at TEXT,
    interview_at TEXT,
    rejected_at TEXT,
    follow_up_date TEXT,
    notes TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (job_id) REFERENCES jobs(id)
);

CREATE TABLE IF NOT EXISTS searches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query TEXT NOT NULL,
    location TEXT,
    source TEXT,
    searched_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS job_searches (
    job_id INTEGER NOT NULL,
    search_id INTEGER NOT NULL,
    PRIMARY KEY (job_id, search_id),
    FOREIGN KEY (job_id) REFERENCES jobs(id),
    FOREIGN KEY (search_id) REFERENCES searches(id)
);

CREATE INDEX IF NOT EXISTS idx_jobs_posted_at ON jobs(posted_at);
CREATE INDEX IF NOT EXISTS idx_jobs_company ON jobs(company);
CREATE INDEX IF NOT EXISTS idx_jobs_title ON jobs(title);
CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobs(status);
CREATE INDEX IF NOT EXISTS idx_job_scores_final_score ON job_scores(final_score);
CREATE INDEX IF NOT EXISTS idx_applications_status ON applications(status);
