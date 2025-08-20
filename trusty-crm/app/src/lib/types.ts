export type UUID = string;

export interface Company {
  id: UUID;
  name: string;
  domain?: string;
  logoUrl?: string;
}

export interface Contact {
  id: UUID;
  fullName: string;
  email?: string;
  employer?: string;
  companyId?: UUID | null;
  relationship?: "alumni" | "contact";
}

export interface Application {
  id: UUID;
  companyId: UUID;
  jobTitle?: string;
  status?: "applied" | "interview" | "offer" | "rejected" | "ghosted";
  createdAt: string;
}

export interface Task {
  id: UUID;
  type: "follow_up" | "intro" | "thank_you";
  dueAt: string;
  relatedContactId?: UUID;
  relatedApplicationId?: UUID;
}
