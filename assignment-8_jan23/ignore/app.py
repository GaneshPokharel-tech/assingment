{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "85fc7163-9c74-4701-92a5-73b5f5a47dd1",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-01-25 19:27:18.066 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-25 19:27:18.068 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-25 19:27:18.068 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-25 19:27:18.069 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-25 19:27:18.070 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-25 19:27:18.070 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-25 19:27:18.071 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-25 19:27:18.071 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-25 19:27:18.072 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-25 19:27:18.072 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-25 19:27:18.072 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-01-25 19:27:18.073 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "st.title(\"Decision Integrity for Credit\")\n",
    "\n",
    "st.write(\"Upload model decision output CSV\")\n",
    "\n",
    "file = st.file_uploader(\"Upload CSV\", type=[\"csv\"])\n",
    "\n",
    "if file:\n",
    "    df = pd.read_csv(file)\n",
    "    st.dataframe(df)\n",
    "\n",
    "    if \"decision_tag\" in df.columns:\n",
    "        st.subheader(\"🔴 High Risk Decisions\")\n",
    "        st.dataframe(df[df[\"decision_tag\"] == \"REVIEW\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bd705fd-9d71-44dd-bcbf-7d362a2ac485",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
