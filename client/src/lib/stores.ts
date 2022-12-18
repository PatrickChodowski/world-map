import { writable } from "svelte/store";
import type { Writable } from "svelte/store";


export const LOCAL_SERVER_URL: string = "http://127.0.0.1:8000"
// export const DEV_GCP_SERVER_URL: string = "https://dev.app.datadriven.chalhoub.cloud";
// export const PROD_GCP_SERVER_URL: string = "https://app.datadriven.chalhoub.cloud";
export const SERVER_URL: string = LOCAL_SERVER_URL;

export let show_spinner: Writable<boolean> = writable(false);
