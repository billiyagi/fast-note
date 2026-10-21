"""API catatan sederhana untuk latihan dict, list, dan tuple."""

from itertools import count

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field


app = FastAPI(
    title="Fast Note",
    description=(
        "Belajar struktur data Python melalui aplikasi catatan. "
        "Data disimpan di memori dan hilang saat server dimulai ulang."
    ),
)