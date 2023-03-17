export interface IAccountProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
}

export interface IAccountProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IAccountProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}
