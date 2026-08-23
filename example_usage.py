from client import GitSemanticMergeConflictResolverClient

def main():
    client = GitSemanticMergeConflictResolverClient()
    res = client.resolve_conflicts('main', 'feat/payment-retry')
    print('Merge Verdict: ' + res['merge_verdict'] + ' | Confidence: ' + str(res['confidence_score']) + '%')
    print('Conflicts Resolved: ' + str(res['total_conflicts_resolved']))
    for r in res['resolved_files']:
        print('  [' + r['file'] + '] ' + r['resolution_strategy'] + ' (' + str(r['lines_resolved']) + ' lines, Valid: ' + str(r['syntax_validated']) + ')')

if __name__ == '__main__':
    main()
