import pandas as pd
import plotly.express as px

df = pd.read_csv('../data_examples/session_scores.csv')
fig = px.bar(df, x='agent', y='insight_score', color='agent',
             title='AgentInsight: QA Score by Agent')
fig.write_html('agentinsight_summary.html')
print("✅ Visualization created.")
