# Job Application Tracker

A full-stack web app to track job applications, manage contacts, and get follow-up reminders.

## Tech Stack
- **Frontend**: React + TypeScript, React Query, Zustand, Tailwind CSS
- **Backend**: Node.js, Express, Prisma ORM
- **Database**: PostgreSQL (Supabase)
- **Auth**: JWT + Google OAuth
- **Deploy**: Vercel (client) + Railway (server)

## Getting Started

### Prerequisites
- Node.js 18+
- PostgreSQL database (or Supabase free tier)

### Backend
```bash
cd job-tracker-server
npm install
cp .env.example .env   # fill in your values
npx prisma migrate dev
npm run dev
```

### Frontend
```bash
cd job-tracker-client
npm install
npm run dev
```

## Features
- Add and track job applications by status
- Kanban board view with drag-and-drop
- Notes and contacts per application
- Email reminders for follow-ups
- Stats dashboard (response rates, pipeline breakdown)
