import sentry_sdk

sentry_sdk.init(
    traces_sample_rate=1.0,
    debug=True,
)


def bla():
    raise ValueError


if __name__ == "__main__":
    bla()
