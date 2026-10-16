"""Fail closed if the internal RSS-only pilot accidentally enables extra services."""
import importlib.util
from pathlib import Path
import yaml
c=yaml.safe_load(Path('config/config.yaml').read_text())
assert c['app']['timezone']=='Africa/Johannesburg'
assert c['platforms']['enabled'] is False and c['platforms']['sources']==[]
assert c['rss']['enabled'] is True and len(c['rss']['feeds'])==12
assert c['rss']['freshness_filter']=={'enabled':True,'max_age_days':3}
assert c['filter']['method']=='keyword'
assert c['notification']['enabled'] is False
assert not any(v for ch in c['notification']['channels'].values() for v in ch.values())
assert c['ai_analysis']['enabled'] is False and c['ai_translation']['enabled'] is False
assert not c['ai']['api_key'] and not c['ai']['model']
assert c['storage']['backend']=='local' and c['storage']['local']['retention_days']==14
assert c['storage']['pull']['enabled'] is False
assert importlib.util.find_spec('litellm') is None
assert importlib.util.find_spec('fastmcp') is None
assert sorted(p.name for p in Path('.github/workflows').glob('*'))==['crawler.yml']
from trendradar.core import load_config
from trendradar.core.frequency import load_frequency_words
from trendradar.__main__ import NewsAnalyzer
config=load_config()
groups,_,_=load_frequency_words()
assert len(groups)==2
print('RSS-only import/config/keyword guardrails PASS; AI/MCP dependencies absent')

# Exercise the actual startup gate without fetching any feeds.
analyzer=NewsAnalyzer(config)
assert analyzer._initialize_and_check_config()
assert analyzer._crawl_data()==({}, {}, [])
analyzer.ctx.cleanup()
print('RSS-only startup and zero hotlist calls PASS')
